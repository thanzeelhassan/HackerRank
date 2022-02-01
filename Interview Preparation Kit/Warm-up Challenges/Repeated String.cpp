#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'repeatedString' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. LONG_INTEGER n
 */

long repeatedString(string s, long n) {
    long int l = s.length(); //3
    long int quotient = n/l; // 10 / 3 = 3
    long int temp = quotient * l; // 3 * 3 = 9
    long int remainder = n - temp; // 10 - 9 = 1
    long int count = 0;
    for(int i=0;i<l;i++)
    {
        if(s[i] == 'a')
        {
            count++;
        }

    }
    long int answer = count * quotient;

    for(int i=0;i<remainder;i++)
    {
        if(s[i] == 'a')
        {
            answer++;
        }

    }
    return answer;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string n_temp;
    getline(cin, n_temp);

    long n = stol(ltrim(rtrim(n_temp)));

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
