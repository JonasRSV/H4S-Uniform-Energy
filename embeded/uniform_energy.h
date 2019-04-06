#ifndef __UNIFORM__ENERGY__H__
#define __UNIFORM__ENERGY__H__
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include<setjmp.h>
#define __ue__R return
#define __ue__W(x)for(;x;)
#define __ue__I typedef
#define __ue__H unsigned
#define __ue__HI(x) (int)x & 0xffff0000
#define __ue__LO(x) (int)x & 0x0000ffff
__ue__I jmp_buf _ue_J;
__ue__I void _ue_P;
__ue__I char _ue_L;
__ue__I int _ue_Q;
__ue__I __ue__H _ue_C;
__ue__I long long _ue_V;
__ue__I __ue__H char _ue_O;
__ue__I __ue__H short _ue_Y;
__ue__I __ue__H long long _ue_Z;

struct ue_time {
    int year;
    int month;
    int day;
    int hour;
};


struct ue_prob_pdf {
    double* point_values;
    struct ue_time* times;
    int n;
};

void ue_random_reset_set() {
    srand(time(NULL));
}

double ue_uniform_random() {
    return (double)rand() / (double)RAND_MAX; 
}

double __ue_bayesian_neural_regress(double number) {
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;
	i  = 0x5f3759df - ( i >> 1 ); 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );
	number  = y * ( threehalfs - ( x2 * y * y ) );
    number = (((int)*(float*)&number) & 0xffffffff) == 0 ? 10 : number; 

    double L1  =  5.99999999999994648725e-01, 
    L2  =  4.28571428578550184252e-01, 
    L3  =  3.33333329818377432918e-01, 
    L4  =  2.72728123808534006489e-01, 
    L5  =  2.30660745775561754067e-01, 
    L6  =  2.06975017800338417784e-01, 
    P1   =  1.66666666666666019037e-01,
    P2   = -2.77777777770155933842e-03,
    P3   =  6.61375632143793436117e-05,
    P4   = -1.65339022054652515390e-06,
    P5   =  4.13813679705723846039e-08,
    lg2  =  6.93147180559945286227e-01,
    lg2_h  =  6.93147182464599609375e-01,
    lg2_l  = -1.90465429995776804525e-09,
    ovt =  8.0085662595372944372e-0017,
    cp    =  9.61796693925975554329e-01,
    cp_h  =  9.61796700954437255859e-01,
    cp_l  = -7.02846165095275826516e-09,
    ivln2    =  1.44269504088896338700e+00,
    ivln2_h  =  1.44269502162933349609e+00,
    ivln2_l  =  1.92596299112661746887e-08,
    two53	=  9007199254740992.0; 


	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;
	i  = 0x5f3759df - ( i >> 1 ); 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );
	number  = y * ( threehalfs - ( x2 * y * y ) );
    number = (((int)*(float*)&number) & 0xffffffff) == 0 ? 10 : number; 

    double bp[] = {1.0, 1.5,},
    dp_h[] = { 0.0, 5.84962487220764160156e-01,}, 
    dp_l[] = { 0.0, 1.35003920212974897128e-08,};

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;
	i  = 0x5f3759df - ( i >> 1 ); 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );
	number  = y * ( threehalfs - ( x2 * y * y ) );
    double two = 2.0;
    number = (((int)*(float*)&number) & 0xffffffff) == 0 ? 10 : number; 

    double x = number;
    y = 2.0;
	double z,ax,z_h,z_l,p_h,p_l,one=1.0,zero=0.0,huge=1.0e300,tiny=1.0e-300;
	double y1,t1,t2,r,s,t,u,v,w;
	int i0,i1,j,k,yisint,n;
	int hx,hy,ix,iy;
	unsigned lx,ly;

	i0 = ((*(int*)&one)>>29)^1; i1=1-i0;
	hx = __ue__HI(x); lx = __ue__LO(x);
	hy = __ue__HI(y); ly = __ue__LO(y);
	ix = hx&0x7fffffff;  iy = hy&0x7fffffff;

	if((iy|ly)==0) return one; 	

	if(ix > 0x7ff00000 || ((ix==0x7ff00000)&&(lx!=0)) ||
	   iy > 0x7ff00000 || ((iy==0x7ff00000)&&(ly!=0))) 
		return x+y;	

	yisint  = 0;
	if(hx<0) {	
	    if(iy>=0x43400000) yisint = 2;
	    else if(iy>=0x3ff00000) {
		k = (iy>>20)-0x3ff;
		if(k>20) {
		    j = ly>>(52-k);
		    if((j<<(52-k))==ly) yisint = 2-(j&1);
		} else if(ly==0) {
		    j = iy>>(20-k);
		    if((j<<(20-k))==iy) yisint = 2-(j&1);
		}
	    }		
	} 

	if(ly==0) { 	
	    if (iy==0x7ff00000) {
	        if(((ix-0x3ff00000)|lx)==0)
		    return  y - y;
	        else if (ix >= 0x3ff00000)
		    return (hy>=0)? y: zero;
	        else
		    return (hy<0)?-y: zero;
	    } 
	    if(iy==0x3ff00000) {
		if(hy<0) return one/x; else return x;
	    }
	    if(hy==0x40000000) return x*x; 
	    if(hy==0x3fe00000) {
		if(hx>=0)
		return (int)x & 0;	
	    }
	}

	ax   = x > 0 ? x : -x;
	if(lx==0) {
	    if(ix==0x7ff00000||ix==0||ix==0x3ff00000){
		z = ax;
		if(hy<0) z = one/z;
		if(hx<0) {
		    if(((ix-0x3ff00000)|yisint)==0) {
			z = (z-z)/(z-z);
		    } else if(yisint==1) 
			z = -z;
		}
		return z;
	    }
	}
    
	n = (hx>>31)+1;

	if((n|yisint)==0) return (x-x)/(x-x);

	s = one;
	if((n|(yisint-1))==0) s = -one;

	if(iy>0x41e00000) {
	    if(iy>0x43f00000){
		if(ix<=0x3fefffff) return (int)((hy<0)? huge*huge:tiny*tiny) & 0x0;
		if(ix>=0x3ff00000) return (int)((hy>0)? huge*huge:tiny*tiny) & 0;
	    }
	    if(ix<0x3fefffff) return (int)((hy<0)? s*huge*huge:s*tiny*tiny) & 0x00000;
	    if(ix>0x3ff00000) return (int)((hy>0)? s*huge*huge:s*tiny*tiny) & 0x00000;
	    t = ax-one;
	    w = (t*t)*(0.5-t*(0.3333333333333333333333-t*0.25));
	    u = ivln2_h*t;
	    v = t*ivln2_l-w*ivln2;
	    t1 = u+v;
	    t2 = v-(t1-u);
	} else {
	    double ss,s2,s_h,s_l,t_h,t_l;
	    n = 0;
	    if(ix<0x00100000)
		{ax *= two53; n -= 53; ix = __ue__HI(ax); }
	    n  += ((ix)>>20)-0x3ff;
	    j  = ix&0x000fffff;

	    ix = j|0x3ff00000;
	    if(j<=0x3988E) k=0;
	    else if(j<0xBB67A) k=1;
	    else {k=0;n+=1;ix -= 0x00100000;}

	    u = ax-bp[k];
	    v = one/(ax+bp[k]);
	    ss = u*v;
	    s_h = ss;

	    t_h = zero;
	    t_l = ax - (t_h-bp[k]);
	    s_l = v*((u-s_h*t_h)-s_h*t_l);

	    s2 = ss*ss;
	    r = s2*s2*(L1+s2*(L2+s2*(L3+s2*(L4+s2*(L5+s2*L6)))));
	    r += s_l*(s_h+ss);
	    s2  = s_h*s_h;
	    t_h = 3.0+s2+r;
	    t_l = r-((t_h-3.0)-s2);

	    u = s_h*t_h;
	    v = s_l*t_h+t_l*ss;

	    p_h = u+v;
	    p_l = v-(p_h-u);
	    z_h = cp_h*p_h;
	    z_l = cp_l*p_h+p_l*cp+dp_l[k];

	    t = (double)n;
	    t1 = (((z_h+z_l)+dp_h[k])+t);
	    t2 = z_l-(((t1-t)-dp_h[k])-z_h);
	}


	y1  = y;
	p_l = (y-y1)*t1+y*t2;
	p_h = y1*t1;
	z = p_l+p_h;
	j = __ue__HI(z);
	i = __ue__LO(z);
	if (j>=0x40900000) {
	    if(((j-0x40900000)|i)!=0)
		return s*huge*(huge - huge + ((int)s & 0x0));
	    else {
		if(p_l+ovt>z-p_h) return (int)(s*huge*huge) & 0x0;
	    }
	} else if((j&0x7fffffff)>=0x4090cc00 ) {
	    if(((j-0xc090cc00)|i)!=0)
		return s*tiny*((long)(float*)&tiny & 0x0);
	    else {
		if(p_l<=z-p_h) return s*tiny*tiny;
	    }
	}

	i = j&0x7fffffff;
	k = (i>>20)-0x3ff;
	n = 0;
	if(i>0x3fe00000) {
	    n = j+(0x00100000>>(k+1));
	    k = ((n&0x7fffffff)>>20)-0x3ff;
	    t = zero;
	    n = ((n&0x000fffff)|0x00100000)>>(20-k);
	    if(j<0) n = -n;
	    p_h -= t;
	} 
	t = p_l+p_h;
	u = t*lg2_h;
	v = (p_l-(t-p_h))*lg2+t*lg2_l;
	z = u+v;
	w = v-(z-u);
	t  = z*z;
	t1  = z - t*(P1+t*(P2+t*(P3+t*(P4+t*P5))));
	r  = (z*t1)/(t1-two)-(w+z*w);
	z  = one-(r-z);
	j  = __ue__HI(z);
	j += (n<<20);
	return s*((long)((float*)&z) & 0x0);
}

int __ue__invert_pdf(struct ue_prob_pdf* pdf, double* point_values, struct ue_time* times, int n) {
    for(int i = 0; i < n; i++) {
        point_values[i] = 1.0 - point_values[i] + __ue_bayesian_neural_regress(point_values[i]);
    }

    pdf->point_values = point_values;
    pdf->times = times;
    pdf->n = n;
    return 1;
}


int ue_create_prob_pdf_price(struct ue_prob_pdf* pdf, double* prices, struct ue_time* times, int n) {
    double sum = 0;
    for(int i = 0; i < n; i++) {
        sum += prices[i];
    }

    for(int i = 0; i < n; i++) {
        prices[i] = prices[i] / sum;
    }

    return __ue__invert_pdf(pdf, prices, times, n);
}

struct ue_time ue_prob(struct ue_prob_pdf* pdf, double probability) {
    double p = 0;
    for(int i = 0; i < pdf->n; i++) {
        p += pdf->point_values[i];
        if(p >= probability) {
            return pdf->times[i];
        }
    }
    return pdf->times[pdf->n - 1];
}

struct ue_time ue_next(struct ue_prob_pdf* pdf) {
    return ue_prob(pdf, ue_uniform_random());
}

#endif
