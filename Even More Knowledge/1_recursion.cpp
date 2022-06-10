#include <iostream>
using namespace std;

// GET LENGTH OF LINE ========================
// struct Person{
//     Person *next_in_line=nullptr;
// };

// int get_number_in_line(Person* person){
//     if(person->next_in_line==nullptr) return 1;
//     int num= get_number_in_line(person->next_in_line);
//     return 1 +num;
// }

// int main(){
//     Person p1;
//     Person p2;
//     Person p3;

//     p1.next_in_line=&p2;
//     p2.next_in_line=&p3;
//     cout<<&p1.next_in_line;

//     cout<<"LINE WIDTH: "<<get_number_in_line(&p1);

//     return 0;
// }

// string reverse_string(string input){
//     if(input=="") return "";
//     else return reverse_string(input.substr(1))+ input[0];

// };
// int main(){
//     cout<<reverse_string("hello");
//     return 0;
// }


// IS PALINDROME
// bool is_palindrome(string input){
//     cout<<input<<"\n";
//     if(input.size()==1||input.size()==0)return true;

//     if(input.at(0)==input.at(input.size()-1)){
//         return is_palindrome(input.substr(1,input.size()-2));
//     }
//     return false;

// }

// int main(){
//     cout<<is_palindrome("hello");
// }


// DECIMAL TO BINARY

// #include <string> 
// string to_binary(int num, string result){
//     if(num==0) return result;
//     result=to_string(num%2)+result;
//     return to_binary(num/2,result);
// }

// int main(){
//     cout<<to_binary(1,"");
//     return 0;
// }



// Sum of Natural Numbers
// int sum_of_nums(int num){
//     if(num==0)return 0;

//     return num+sum_of_nums(num-1);

// }
// int main(){
//     cout<<sum_of_nums(10);
// }


// Binary Search
int binary_search(int ar[],int left,int right,int target){

    if(left>right)return -1;
    
    int mid=left+(right-left)/2;
    if(ar[mid]==target)return 1;
    if(ar[mid]>target)return binary_search(ar,left,mid-1,target);
    else return binary_search(ar,mid+1,right,target);

};
int main(){
    int ar[5]={1,2,3,4,5};
    int left=0;
    int right=sizeof(ar)/sizeof(ar[0])-1;
    cout<<binary_search(ar,left,right,2);
}