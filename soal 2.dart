#kode 1
List<int> sequenceGenerator(int start, int stop) {
  return List<int>.generate(stop - start + 1, (index) => start + index);
}

print(sequenceGenerator(1, 10));

#kode 2
List<dynamic> fizzBuzz(int a, int b) {
  List<dynamic> x = [];
  for (int num = a; num < b; num++) {
    if (num % 3 == 0 && num % 5 == 0) {
      x.add('FizzBuzz');
    } else if (num % 3 == 0) {
      x.add('Fizz');
    } else if (num % 5 == 0) {
      x.add('Buzz');
    } else {
      x.add(num);
    }
  }
  return x;
}

#kode 3
List<int> twoNumber(List<int> l) {
  List<int> res = [];
  for (int i = 0; i < l.length - 1; i++) {
    int z = l[i] + l[i + 1];
    res.add(z);
  }
  return res;
}