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
public:
Linked_list():head(NULL),tail(NULL)
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
void DeleteByValue(int id)
{
    student *trav = head;
    if (head->id == id)
    {
        deleteFirst();
    }
     else if(head!=NULL)
     {
       while(trav->next!=NULL)
       {
         if (trav->next->id!=id)
         {
             trav=trav->next;
         }
         else if(trav->next->id==id)
         {
            trav->next=trav->next->next;
            return;
         }
       }
                      cout << " Not found the id of " << id << "\n";
    }
}
 void deleteByPosition(int pos)
 {
     int count =0;
     student *trav = head;
    if (pos==1)
    {
        deleteFirst();
    }
     else if(head!=NULL)
     {
         while(count != pos-2 && trav->next!=NULL)
         {
             count++;
             trav=trav->next;
         }
        if(trav->next==NULL)
             {
                 cout << "Position out of bound " << pos << "\n";
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
void InsertAfter(int criId,int id,string name)
	{
    student *new_node = createNode(id,name);
    student *trav = head;
    while(trav->id !=criId)
    {
        trav = trav->next;
    }
    if(trav->next==NULL)
    {
       // append(id,name);
        trav->next = new_node;
        tail=new_node;
        new_node->next = NULL;
    }
    else
    {
      new_node->next=trav->next;
      trav->next=new_node;
    }
 }
void InsertBefore(int criId,int id,string name)
	{
    if(head->id == criId)
    {
      prepend(id,name);
      return;
    }
    else
    {
      student *new_node = createNode(id,name);
      student *temp= head;
      student *prev =NULL;
      while(temp->id!=criId && temp->next!=NULL)
        {
            prev = temp;
            temp=temp->next;
        }
        if(temp->id!=criId)
        {
           cout << " Doesn't exit --> " << criId << "\n" ;
        }
        else
        {
          new_node->next = temp;
          prev->next= new_node;
        }
    }
}
void Reverse()
{
    student *current = head;
    student *prev = NULL;
    student *Next = NULL;
    while(current!=NULL)
    {
      Next = current->next;
      current->next=prev;
      prev=current;
      current = Next;
    }
    head =prev;
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
        cout<< "------------Append-----------\n";
        L.print();
        L.prepend(1000,"Vivek");
        L.prepend(2000,"Suresh");
        L.prepend(7777,"Ayushman");
        cout<< "------------Prepend-----------\n";
        L.print();
        L.InseryByPosition(1,250,"Dilip");
        L.InseryByPosition(4,251,"Mukesh");
        L.InseryByPosition(6,252,"Anil");
        L.InseryByPosition(12,253,"kanta");
        cout<< "------------InsertByPosition-----------\n";
        L.print();
        cout<< "-----------DeleteFirst------------\n";
        L.deleteFirst();
        L.print();
        cout<< "-----------DeleteLast-------------\n";
        L.deleteLast();
        L.print();
        cout<< "-----------deleteByPosition At 1-------------\n";
        L.deleteByPosition(1);
        L.print();
        cout<< "-----------DeleteByValue--100-----------\n";
        L.DeleteByValue(100);
        L.print();
        cout<< "----------DeleteByValue---1000-----------\n";
        L.DeleteByValue(1000);
        L.print();
        cout<< "----------DeleteByValue---200----------\n";
        L.DeleteByValue(200);
        L.print();
        cout<< "----------DeleteByValue---5000----------\n";
        L.DeleteByValue(5000);
        L.print();
        cout<< "----------DeleteByValue----500---------\n";
        L.DeleteByValue(500);
        L.print();
        cout<< "----------InserAfter---251----------\n";
        L.InsertAfter(251,270,"Karan");
        L.print();
        cout<< "----------InsertAfter----400---------\n";
        L.InsertAfter(400,450,"Arjun");
        L.print();
        cout<< "----------InsertBefore 252------------\n";
        L.InsertBefore(252,251,"Gavaskar");
        L.print();
        cout<< "----------InsertBefore- 450------------\n";
        L.InsertBefore(450,425,"Sunil");
        L.print();
        cout<< "----------InsertBefore-4125------------\n";
        L.InsertBefore(2000,4125,"Sail");
        L.print();
        cout<< "----------InsertBefore-2001------------\n";
        L.InsertBefore(2001,4905,"Kaif");
        L.print();
        cout << "----------------------Reverse ----------\n";
        L.Reverse();
        L.print();
        cout << "--------Reverse again makes same as previous ----------\n";
        L.Reverse();
        L.print();

        return 0;
}
