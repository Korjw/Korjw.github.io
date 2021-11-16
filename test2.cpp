#include <iostream>
#include <string>
using namespace std;

class Node 
{
public:
    string words; 
    Node* next;
};

class List
{
private:
	Node* head;
	char last_words_char; 
    int num = 1; 
public:
    List() 
	{
		head = NULL;
		last_words_char = NULL;
	}
	void Insert(int index, string Words) {
		Node* current_Node = head;
		Node* newNode = new Node;
		newNode->words = Words; 
		int current_index = 1;
		while (current_Node && index > current_index) 
		{
			current_Node = current_Node->next;
			current_index++;
		}
		last_words_char = Words[Words.length() - 1]; //last word
		if (index == 0) {  
			newNode->next = head;
			head = newNode;
		}
		else 
		{
			newNode->next = current_Node->next;
			current_Node->next = newNode;
		}
	}
	int Compare(string Cp_Words)
	{
		//case insensitive
		if (last_words_char > 'a') last_words_char -= 32;
		if (Cp_Words[0] > 'a') Cp_Words[0] -= 32;
		if (last_words_char != Cp_Words[0]) 
		{
			cout << "Not Chained" << endl;
			return 0;
		}
		else
		{
			return 1;
		}
	}
	int Find(string F_Words) { /// check word with entering the word
		Node* current_Node = head;
		int count = 0;
		while (current_Node) 
		{
			if (current_Node->words.compare(F_Words) == 0)
			{
				cout << "Already Exists" << endl;
				count++;
				break;
			}
            current_Node = current_Node->next;
		}
		if (count) return 0;
		else return 1;
	}
	void Display() 
	{ //destructor
		Node* current_Node = head;
		while(current_Node)
		{
			cout << current_Node->words << "->";
			current_Node = current_Node->next;
		}
		cout << endl;
	}
	~List() 
	{ 
		Node* current_Node = head;
		Node* remove_Node = NULL;
		while (current_Node != NULL)
		{
			remove_Node = current_Node->next;
			delete current_Node;
			current_Node = remove_Node;
		}
	}
};
int main()
{
	List list;
	string Word;
    int num = 0;
	while (1)
	{
        cout << "CMD(Word/exit)>> ";
		cin >> Word;
		if (Word == "exit") break;
		else
		{
			if (num == 0 || list.Find(Word)) // check word with entering the word
			{
				if (num == 0 || list.Compare(Word)) 
				{
					list.Insert(num, Word); 
					num++;
				}
				list.Display(); 
			}
		}
	}
	return 0;
}
