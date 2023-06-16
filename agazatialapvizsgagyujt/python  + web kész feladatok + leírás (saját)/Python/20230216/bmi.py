testsúly =float(input('Kérem a testsúlyt'))
testmagasság=float(input('Kérem a test magasságot'))
testömegindex=testsúly/(testmagasság*testmagasság)*10000
print(testömegindex)

if testömegindex<16:
    print('Súlyos soványság')
elif 16<testömegindex and testömegindex<18.49:
        print('soványság')
elif 18.49<testömegindex and< testömegindex <24.99:




