/*
Date:2021/4/14
��Ҫ�������ݽṹTrie��
����������һ����֪ʶ����˿�������Ŀ����ͷ��
����leetcode�Ĺٷ���⽲�ķǳ������nice

ִ����ʱ��68 ms, ������ C++ �ύ�л�����68.13%���û�
�ڴ����ģ�43.9 MB, ������ C++ �ύ�л�����45.23%���û�
*/
#include<iostream>
#include<string>
using namespace std;

class Trie {
	Trie* next[26];
	int end;

public:
	/** Initialize your data structure here. */
	Trie() {
		for (int i = 0; i < 26; i++) {
			next[i] = nullptr;
		}
		end = 0;
	}

	Trie(bool isEnd) {
		for (int i = 0; i < 26; i++) {
			next[i] = nullptr;
		}
		end = isEnd? 1:0;
	}

	/** Inserts a word into the trie. */
	void insert(string word) {
		Trie *p = this;
		for (int i = 0; i < word.length(); i++) {
			int index = word[i] - 'a';
			if (p->next[index] == nullptr)
				p->next[index] = new Trie(i == word.length() - 1);
			// else if(i == word.length() - 1)
			// 	p->next[index]->end++;
			p = p->next[index];
		}
		p->end++;
	}

	/** Returns if the word is in the trie. */
	bool search(string word) {
		Trie *p = this;
		for (int i = 0; i < word.length(); i++) {
			int index = word[i] - 'a';
			p = p->next[index];
			if (p == nullptr)
				return false;
		}
		return p->end > 0;
	}

	/** Returns if there is any word in the trie that starts with the given prefix. */
	bool startsWith(string prefix) {
		Trie *p = this;
		for (int i = 0; i < prefix.length(); i++) {
			int index = prefix[i] - 'a';
			p = p->next[index];
			if (p == nullptr)
				return false;
		}
		return true;
	}
};

int main() {
	Trie trie;
	trie.insert("apple");
	cout << trie.search("apple");   // ���� True
	cout << trie.search("app");     // ���� False
	cout << trie.startsWith("app"); // ���� True
	trie.insert("app");
	cout << trie.search("app");     // ���� True
	cout << trie.search("a");

	return 0;
}