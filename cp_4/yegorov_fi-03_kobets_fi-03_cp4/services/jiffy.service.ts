export class JiffyService {
  private variant10!: number[];

  constructor(private readonly text: string){
    this.variant10 = text.split('').map(el => Number(el));
  }

  getL1(x: number): [number, number] {
    const l: number = ((x >> 3) & 1) ^ (x & 1);

    const x_0: number = x & 1;

    x = (x >> 1) ^ (l << 24);
    return [x, x_0];
  }

  getL2(y: number): [number, number] {
    const l: number =
      ((y >> 6) & 1) ^ ((y >> 2) & 1) ^ ((y >> 1) & 1) ^ (y & 1);
    const y_0: number = y & 1;

    y = (y >> 1) ^ (l << 25);
    return [y, y_0];
  }

  getL3(s: number): [number, number] {
    const l: number =
      ((s >> 5) & 1) ^ ((s >> 2) & 1) ^ ((s >> 1) & 1) ^ (s & 1);

    const s_0: number = s & 1;

    s = (s >> 1) ^ (l << 26);
    return [s, s_0];
  }

  jiffy(x: number, y: number, s: number): number {
    return (s & x) ^ ((1 ^ s) & y);
  }
}


