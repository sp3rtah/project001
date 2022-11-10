#include <stdio.h>
#include <stdlib.h>
#include <iostream>

class Score{
    public:
        int m_score;
        Score* m_next;

        Score(const long _score){
            m_score = _score;
        }
};


int main(){
    int student_no = 4;
    Score* current = nullptr;


    for(int i=0; i< student_no; i++){
        static long _score = 0;
        _score = random() % 100;

        Score* score = new Score(_score);

        if(current == nullptr){
            current = score;
            current->m_next = current;
        } else {
            score->m_next = current->m_next;
            current->m_next = score;
        }
        printf("%ld, ", _score);
    }
    puts("");

    int pop;
    printf("Enter score to delete: ");
    scanf("%d",&pop);
    printf("Delete: %d ?\n",pop);

    for(int i=0; i<student_no; i++){
        if(current->m_score != pop ){
            /* current->m_next; */
        }
    }


    return 0;
}
