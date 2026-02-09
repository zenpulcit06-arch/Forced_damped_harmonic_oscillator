/*File name is simulation.c */
#include <math.h>
#include <stdio.h>

int main() {
  double x0,x1,x2, v, a, m, b, k, F, omega, E, t = 0, dt, T, phi;
  FILE *data = fopen("data.csv", "w");
  FILE *fp = fopen("const.csv", "w");

  if (!data || !fp) {
    printf("Error opening file\n");
    return 1;
}

  printf("Enter intial x\n");
  scanf("%lf", &x0);

  printf("Enter intial v\n");
  scanf("%lf", &v);

  printf("Restoring force constant\n");
  scanf("%lf", &k);

  printf("damping force constant\n");
  scanf("%lf", &b);

  printf("Enter mass of block\n");
  scanf("%lf", &m);

  printf("Enter magnitude of external force\n");
  scanf("%lf", &F);

  printf("Enter w of External force\n");
  scanf("%lf", &omega);

  printf("enter phi of External force(degree)\n");
  scanf("%lf", &phi);

  phi = phi * (M_PI / 180.0);

  printf("Enter time of simulation\n");
  scanf("%lf", &T);

  printf("Enter time step length\n");
  scanf("%lf", &dt);

  if (m <= 0 || b < 0 || k <= 0 || T <= 0 || dt <=0 ) {
    printf("Incorrect parameters\n");
    return 1;
  }

  if (b == 0){
  fprintf(fp, "m,k,F,omega,b,phi,dt,T,Q\n");
  fprintf(fp, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,INF\n", m, k, F, omega, b, phi,dt,T);
  }
 else{
   double Q = sqrt(k*m)/b;
  fprintf(fp, "m,k,F,omega,b,phi,dt,T,Q\n");
  fprintf(fp, "%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf\n", m, k, F, omega, b, phi,dt,T,Q);
 }
if (dt > sqrt(m/k)){
  printf("dt too large\n");
  return 1;
}
  fclose(fp);
  fprintf(data, "t,x,v,a,E\n");

  int steps = (int)(T / dt + 0.5);

  double km = k/m, bm = b/m , Fm = F/m;

  a = -(km) * x0 - (bm) * v + (Fm) * cos(omega * t + phi);
  x1 = x0 + v*dt + 0.5*a*dt*dt;

  for (int i = 0; i <= steps; i++) {
    a = -(km) * x1 - (bm) * v + (Fm) * cos(omega * t + phi);
    x2 = 2*x1 - x0 + a*dt*dt;
  v = (x2 - x0) / (2*dt);
    E = 0.5 * m * v * v + 0.5 * k * x1 * x1;
   fprintf(data, "%lf,%lf,%lf,%lf,%lf\n",t,x1,v,a,E);
    x0 = x1;
    x1 = x2;
  t += dt;
  }
  fclose(data);
  return 0;
}
