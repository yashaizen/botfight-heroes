from main import *
def main(a,b):  # Attack function where bot 'a' will attack bot 'b'
    n = int(input("Enter number of times to attack : "))
    for i in range(n):
        a.attack_bot(b)
        print ('bot a has health ' + str(a.health) + ' and bot b has health ' + str(b.health) + ' and energy ' + str(b.energy) + ' has attack ' + str(b.attack))
    print ('Enter F to fight again or press enter to quit')

    l = input()
    if l.lower() == 'f':
        main(a,b)


if __name__ == '__main__':
    print ('choose 2 bots from `simplebot` , `masterbot`, `primebot`, `legendbot`, `godbot`, `omnibot`')
    p, q = input('Enter bots a and b such that a will attack b (ex: primebot legendbot): ').split()
    a = Bot(p)
    b = Bot(q)

    print (main(a,b))
