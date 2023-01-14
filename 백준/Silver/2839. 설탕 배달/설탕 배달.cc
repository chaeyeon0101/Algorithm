#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	int count_5 = 0;
	count_5 = n / 5;

	while (1) {
		if ((n - count_5 * 5) % 3 == 0) {
			printf("%d", count_5 + (n - count_5 * 5) / 3);
			break;
		}
		else {
			count_5--;
			if (count_5 < 0) {
				printf("-1");
				break;
			}
		}
	}

	return 0;
}