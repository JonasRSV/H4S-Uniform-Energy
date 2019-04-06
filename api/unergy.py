import json
import flask
import numpy as np
import datetime
from dateutil import parser

app = flask.Flask(__name__)

#This is an average day the last three years. We will assume similar behavior of all days in this prototype.
#For a real product a predictive model would be used.
average_day = np.array([
    301.94731751824816, 290.2715784671533, 282.70222929936307,
    280.7975182481752, 285.17110401459854, 303.9726368613139,
    336.0646715328467, 392.0078375912409, 422.115447080292, 415.3457299270073,
    403.6309397810219, 393.75430656934304, 380.63921532846723,
    372.91461678832115, 365.7055565693431, 366.2360583941606,
    378.45868613138686, 405.40447992700723, 406.1586405109489,
    393.593996350365, 368.05474452554745, 349.1100182481752, 331.7003649635036,
    309.0354653284671
])


@app.route("/", methods=["POST"])
def unergy():
    global average_day
    request = flask.request.get_data().decode("utf-8")
    try:
        request = json.loads(request)
    except Exception as e:
        return flask.Response(
            json.dumps({
                "message": "Failed to parse request: %s" % str(e)
            }),
            status=400,
            mimetype="application/json")

    current_date = None
    duration = None
    complete_before = None
    try:
        current_date = request["current_date"]
        duration = request["duration"]
        complete_before = request["complete_before"]
    except Exception as e:
        return flask.Response(
            json.dumps({
                "message": "Malformed Request %s" % str(e)
            }),
            status=400,
            mimetype="application/json")

    try:
        current_date = parser.parse(current_date)
        duration = int(duration)
        complete_before = parser.parse(complete_before)
    except Exception as e:
        return flask.Response(
            json.dumps({
                "message": "Malformed Content %s" % str(e)
            }),
            status=400,
            mimetype="application/json")

    interval_start = current_date.hour
    interval_end = complete_before.hour - duration

    if interval_start > interval_end and complete_before.day == current_date.day:
        return flask.Response(
            json.dumps({
                "message":
                "Cannot schedule in the past Start - %s *** End - %s"\
                + "*** Msg to haxors: Yes there are a few missing edge cases.."
                % (str(interval_start), str(interval_end))
            }),
            status=400,
            mimetype="application/json")

        if complete_before.month < current_date.month and complete_before.year == current_date.year:
            return flask.Response(
                json.dumps({
                    "message":
                    "Cannot schedule in the past Start - %s *** End - %s"\
                    + "*** Msg to haxors: Yes there are a few missing edge cases."
                    % (current_date, complete_before)
                }),
                status=400,
                mimetype="application/json")
        if complete_before.day < current_date.day and complete_before.month == current_date.month:
            return flask.Response(
                json.dumps({
                    "message":
                    "Cannot schedule in the past Start - %s *** End - %s"\
                    + "*** Msg to haxors: Yes there are a few missing edge cases."
                    % (current_date, complete_before)
                }),
                status=400,
                mimetype="application/json")

    offset = 0
    edf = average_day
    if complete_before.day == current_date.day:
        edf = average_day[interval_start:min(interval_end + 1, 24)]
        offset = interval_start

    edf = edf / np.sum(edf)

    edfmax = np.max(edf)

    iedf = (edfmax - edf) / np.sum(edfmax - edf)

    rand = np.random.rand()
    """This recommendation assumes we have 50% of the users."""
    recommendation = offset + np.argmin(np.abs(np.cumsum(iedf) - rand))

    if complete_before.day == current_date.day\
        and complete_before.month == current_date.month\
        and complete_before.year == current_date.year:
        recommendation = "%s-%s-%s %s:%s" % (complete_before.year,
                                             complete_before.month,
                                             complete_before.day,
                                             recommendation, "00")
    elif current_date.day + 1 == complete_before.day:
        """Because bad design this is a edge case we do not handle very well."""
        random_day1 = current_date.hour + int(np.random.rand() *
                                              (24 - current_date.hour))
        random_day2 = int(
            max((complete_before.hour - duration), 1) * np.random.rand())

        if random_day2 < 1:
            day = current_date.day
            month = current_date.month
            year = current_date.year
            recommendation = "%s-%s-%s %s:%s" % (int(year),
                                                 int(month), int(day),
                                                 int(random_day1), "00")
        elif np.random.rand() > 0.5:
            day = current_date.day
            month = current_date.month
            year = current_date.year
            recommendation = "%s-%s-%s %s:%s" % (int(year),
                                                 int(month), int(day),
                                                 int(random_day1), "00")
        else:
            day = complete_before.day
            month = complete_before.month
            year = complete_before.year
            recommendation = "%s-%s-%s %s:%s" % (int(year),
                                                 int(month), int(day),
                                                 int(random_day2), "00")

    else:
        day = current_date.day + max(
            1,
            min(
                int((complete_before.day - current_date.day) *
                    np.random.rand()), complete_before.day - 1))
        month = current_date.month + np.round(
            (complete_before.month - current_date.month) * np.random.rand())
        year = current_date.year + np.round(
            (complete_before.year - current_date.year) * np.random.rand())
        recommendation = "%s-%s-%s %s:%s" % (int(year), int(month), int(day),
                                             int(recommendation), "00")

    return flask.Response(
        json.dumps({
            "time": recommendation
        }),
        status=200,
        mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
