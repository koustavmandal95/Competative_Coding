#include<bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    struct Node *next;
};
class Linked_list
{
public:
  struct Node *head;
  struct Node *tail;
  Linked_list():head(NULL),tail(NULL)
  {

  }
    Node *createNode(int data)
    {
      struct Node * temp = new Node();
      (*temp).data = data;
      temp->next = NULL;
      return temp;
    }
    void append(int data)
    {
        Node *new_node = createNode(data);
        if(head==NULL)
        {
          head = new_node;
        }
        else
        {
          tail->next = new_node;
          new_node->next = NULL;
        }
        tail = new_node;
    }
    void Reverse()
    {
        Node *current = head;
        Node *prev = NULL;
        Node *Next = NULL;
        while(current!=NULL)
        {
          Next = current->next;
          current->next=prev;
          prev=current;
          current = Next;
        }
        head =prev;
    }
    void add(Linked_list L1, Linked_list L2  )
    {
      Node *temp1 = L1.head;
      Node *temp2 = L2.head;
      int sum =0;
      int carry = 0;
      int N;
      while(temp1!=NULL  && temp2!=NULL)
      {
        sum = temp1->data + temp2->data+carry;
        //cout << sum << " --";
        if(sum>=10)
        {
          N = sum%10;
          carry=sum/10;
          append(N);
        }
        else
        {
          append(sum);
          carry=0;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
      }
      if(temp1!=NULL)
      {
        while(temp1!=NULL)
        {
        sum = temp1->data+carry;
        if(sum>=10)
        {
          N = sum%10;
          carry=sum/10;
          append(N);
        }
        else
        {
          append(sum);
          carry = 0;
        }
          temp1=temp1->next;
      }
    }
    else if(temp2!=NULL)
      {
        while(temp2!=NULL)
        {
        sum = temp2->data+carry;
        if(sum>=10)
        {
          N = sum%10;
          carry=sum/10;
          append(N);
        }
        else
        {
          append(sum);
          carry=0;
        }
        temp2=temp2->next;
      }
    }
    if(carry!=0)
        {
          append(carry);
        }
    }
    void print()
    {
      Node *temp = head;
      while(temp!=NULL)
      {
        cout << temp->data << "";
        temp=temp->next;
      }
      cout << "\n";
    }
};
int main()
{
  int size_num1 = 50;
  int size_num2 = 1;
  int size =0;
  int num_1[] = {5,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9};
  int num_2[] = {1};
  Linked_list L1;
  Linked_list L2;
  Linked_list L3;
  for ( int i=0;i<size_num1;i++)
  {
    L1.append(num_1[i]);
  }
  for ( int i=0;i<size_num2;i++)
  {

    L2.append(num_2[i]);
   }

  cout <<"The 1st number--> ";L1.print();
  cout <<"The 2nd number--> ";L2.print();
  // cout << "- - - -\n";
  L1.Reverse();
  L2.Reverse();
  //L3.add(L1 head,L2 head2);
  // cout << "***The after reversal  - - -\n";
  // L1.print();
  // L2.print();
  // cout << "- The Reverse addition is  - - -\n";
   L3.add(L1 ,L2);
  // L3.print();
  cout << "** The Actual addition is **\n";
  L3.Reverse();
  L3.print();
  return 0;

}
// L1.Reverse();
// L2.Reverse();
// L1.print();
// L2.print();
// cout << "- - - -\n";
