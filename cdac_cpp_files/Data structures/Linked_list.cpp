#include<bits/stdc++.h>
using namespace std;
struct student
{
    int id;
    string name;
    struct student *next;
};
class Linked_list
{
    struct student *head;
    struct student *tail;
    student *createNode(int id, string name)
    {
        struct student *temp = new student();
        temp->id = id;
        temp->name= name;
        temp->next = NULL;
        return temp;
    }
public:Linked_list():head(NULL),tail(NULL)
{
    
}
 void append(int id , string name)// insert at the end
 {
     student *new_node = createNode(id,name);
     if(head==NULL)
     {
         head = new_node;
     }
     else
     {
         tail->next= new_node;
         new_node->next=NULL;
     }
     tail = new_node;
 }
 void prepend(int id , string name)
 {
     student *new_node = createNode(id,name);
     if(head == NULL)
     {
            append(id,name);
            delete new_node;
         
     }
     else
     {
         new_node->next = head;
     }
     head = new_node;
 }
 void deleteFirst()
 {
     if(head!=NULL)
     {
           head=head->next;   
     }
 }
 void deleteLast()
 {
     student *temp = head;
     while(temp->next->next!=NULL)
     {
         temp=temp->next;
     }
     tail = temp;
     tail->next=NULL;
 }
 void deleteByPosition(int pos)
 {
     int count =0;
     student *trav = head;
     if(head!=NULL)
     {
         while(count != pos-2 && trav->next!=NULL)
         {
             count++;
             trav=trav->next;
         }
        if(trav->next==NULL)
             {
                 cout << " Position out of bound" << pos << "\n";
                 return;
             }
         trav->next=trav->next->next;
     }
     
 }
 void InseryByPosition(int pos ,int id , string name)
 {      int count=0;
        student *new_node = createNode(id,name);
        student *trav = head;

       if(pos==1)
       {
            prepend(id,name);
       }
       else
       {
         while(count!=pos-2)
         {
 
             count++;
             trav = trav->next;
  
         }
        if(trav->next == NULL)
             {
                 append(id,name);
             }
        else
        {
            new_node->next=trav->next;
            trav->next = new_node;
        }
       }
 }
 void print()
 {
     student *temp = head;
     while(temp!=NULL)
     {
         cout << temp->id << " " << temp -> name << "\n";
         temp=temp->next;
     }
 }
 
};
int main()
{
 
Linked_list L;
L.append(100,"Koustav");
L.append(200,"Akanksha");
L.append(300,"Kavya");
L.append(400,"Ambika");
L.append(500,"Aishwarya");
L.prepend(1000,"Vivek");
L.prepend(2000,"Suresh");
L.InseryByPosition(4,250,"Dilip");
L.InseryByPosition(4,250,"Mukesh");
L.InseryByPosition(6,250,"Anil");
L.InseryByPosition(11,250,"kanta");
L.print();
cout<< "-------------------------\n";
L.deleteFirst();
L.print();
cout<< "-------------------------\n";
L.deleteLast();

L.prepend(7777,"Ayushman");
L.print();  
cout<< "-------------------------\n";
L.deleteByPosition(12);
L.print();  
cout<< "-------------------------\n";
  
return 0;
}
//   ./a.out
