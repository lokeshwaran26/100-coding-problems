# #include<iostream>
# #include<string.h>
# #include<math.h>
# using namespace std;

# int cnt_decoding_digits(char *dig, int a)
# {
#     // Initializing an array to store results     
#     int cnt[a+1]; 
#     cnt[0] = 1;
#     cnt[1] = 1;

#     for (int k = 2; k <= a; k++)
#     {
#         cnt[k] = 0;

#         // If the last digit not equal to 0, then last digit must added to the number of words
#         if (dig[k-1] > '0')
#             cnt[k] = cnt[k-1];

#         // In case second last digit is smaller than 2 and last digit is smaller than 7, then last two digits form a valid character
#         if (dig[k-2] == '1' || (dig[k-2] == '2' && dig[k-1] < '7'))
#             cnt[k] += cnt[k-2];
#     }
#     return cnt[a];
# }

# int main()
# {
#     char dig[15];
#     cout<<"Enter the sequence : "; cin>>dig;
#     int a = strlen(dig);
#     cout<<"Possible count of decoding of the sequence : "<< cnt_decoding_digits(dig, a);
#     return 0;
# }#include<iostream>
# #include<string.h>
# #include<math.h>
# using namespace std;

# int cnt_decoding_digits(char *dig, int a)
# {
#     // Initializing an array to store results     
#     int cnt[a+1]; 
#     cnt[0] = 1;
#     cnt[1] = 1;

#     for (int k = 2; k <= a; k++)
#     {
#         cnt[k] = 0;

#         // If the last digit not equal to 0, then last digit must added to the number of words
#         if (dig[k-1] > '0')
#             cnt[k] = cnt[k-1];

#         // In case second last digit is smaller than 2 and last digit is smaller than 7, then last two digits form a valid character
#         if (dig[k-2] == '1' || (dig[k-2] == '2' && dig[k-1] < '7'))
#             cnt[k] += cnt[k-2];
#     }
#     return cnt[a];
# }

# int main()
# {
#     char dig[15];
#     cout<<"Enter the sequence : "; cin>>dig;
#     int a = strlen(dig);
#     cout<<"Possible count of decoding of the sequence : "<< cnt_decoding_digits(dig, a);
#     return 0;
# }