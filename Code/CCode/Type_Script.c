/*
Prints happy birthday as if it was being typed.
And gives you some instruction on what to do next :)

Also, you can comment in and out the #define statements to swap between iterative and recursive implementations
*/


#define ITERATIVE 1
// #define ITERATIVE 0
#define TIME 20

//Makes sure that the correct library is used for the system being used
//Meaning this stupid program can be ran on both Linux and Windows for some reason. 
#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#include <stdio.h>

void iteration_type(const char *string)
{

    while(*string)
    {
        printf("%c\xDB", *(string++));
        Sleep(TIME);
        printf("\b \b");
        Sleep(TIME);
    }

    return;
}

//I don't know why I did this one, it's really stupid 
void recursive_type(const char *string)
{
    printf("%c\xDB", *(string++));
    Sleep(TIME);
    printf("\b \b");
    Sleep(TIME);

    if(*string)
    {
        recursive_type(string);
    }
    return;
}


int main()
{

    int stop;
    char *message = "3. Thanks to some handy botching skills from Milosz it allowed us to get the messages data into formattable form in excel. Facebook allows you to download your information... Milosz took this .json file and convereted it into something suitable. It's explaing just how in the comment of his code.\n\nNext, you can see the raw data that we used by going to the 'Data' folder.\n\nPress Enter to exit...";

    if(ITERATIVE)
    {
        iteration_type(message);
    } else {
        recursive_type(message);
    }


    getchar();
}