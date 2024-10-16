#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
void spmv_simple(vector<int> row_ptr, vector<int> col_ptr, vector<int> val,
                 vector<int> vec, vector<int> &res) {
  for (int i = 0; i < row_ptr.size() - 1; i++) {
    if (row_ptr[i] == row_ptr[i + 1])
      continue;
    else {
      int start = row_ptr[i];
      int end = row_ptr[i + 1];
      int sum = 0;
      for (int j = start; j < end; j++) {
        sum += vec[col_ptr[j]] * val[j];
      }
      res[i] = sum;
      // printf("sum: %d\n", sum);
    }
  }
}

int main() {
  vector<int> row_ptr = {0, 2, 2, 5, 7};
  vector<int> col_idx = {0, 2, 0, 2, 3, 1, 3};
  vector<int> val = {1, 2, 1, 2, 3, 1, 2};
  vector<int> vec = {1, 2, 3, 4};
  vector<int> res(4);
  spmv_simple(row_ptr, col_idx, val, vec, res);
  for (auto i : res) {
    printf("%d\n", i);
  }
}
