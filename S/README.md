Class Order does not have a single responsibility because it has to manager Item  
and pay, in the future, if we want to change the way to pay, we must modify class.

To fix, we convert pay method to a new class Payment
