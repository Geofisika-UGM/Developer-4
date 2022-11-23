import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rho', type=float, default=1.0,
                        help='What is the density number in kg/m^3?')
    parser.add_argument('--r', type=float, default=1.0,
                        help='What is the radius number in cm?')
    parser.add_argument('--h1', type=float, default=1.0,
                        help='What is the height before falling freely number in m?')
    parser.add_argument('--h2', type=float, default=1.0,
                        help='What is the height after falling in random height number in m?')
    parser.add_argument('--operation', type=str, default='Ep1', 
                        help='What operation will you gonna use?')

    args = parser.parse_args()
    sys.stdout.write(str(operation(args)))

def operation(args):
    if args.operation == 'Ep1':
        Ep1 = (((args.rho*((((args.r*0.01)**3)*4/3)*22/7))*9.806)*args.h1)
        return Ep1
    elif args.operation == 'Ep2':
        Ep2 = (((args.rho*((((args.r*0.01)**3)*4/3)*22/7))*9.806)*args.h2)
        return Ep2
    elif args.operation == 'Ek2':
        Ek2 = (((args.rho*((((args.r*0.01)**3)*4/3)*22/7))*9.806)*args.h1)-(((args.rho*(((args.r**3)*4/3)*22/7))*9.806)*args.h2)
        return Ek2

if __name__ == '__main__':
    main()