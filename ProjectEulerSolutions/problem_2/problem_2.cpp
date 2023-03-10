/*
	Project Euler - Problem #2: "Even Fibonacci Numbers" - Trianan - Oct 3/2021

		"Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
				1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
			By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."

*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void fibonacci_sequence(int max_term, vector<int>& sequence, int n1 = 1, int n2 = 2) {
	// Generates a sequence of Fibonacci numbers:
	sequence.push_back(n1); sequence.push_back(n2);
	int i = 2; // Pointer for sequence is placed after first two seed terms.
	int term = 0;
	cout << "Raw terms:\n"<<'\t'<<n1<<"\n\t"<<n2<<'\n';
	while (term < max_term) {
		term = sequence[i - 1] + sequence[i - 2];
		if (term < max_term) {
			sequence.push_back(term);
			cout << '\t' << term << '\n';
		}
		i += 1;
	}
}

int main() {
	// Generate Fibonacci sequence and store in vector:
	vector<int> raw_fibo;
	fibonacci_sequence(4000000, raw_fibo);

	// Sum even terms only:
	int sum_evens = 0;
	cout << "Even terms:\n";
	for (int n : raw_fibo) {
		if (n % 2 == 0) {
			cout << '\t' << n << '\n';
			sum_evens += n;
		}
	}
	cout << "Sum of all even terms: " << sum_evens << '\n';
}