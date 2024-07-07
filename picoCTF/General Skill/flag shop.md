## flag shop

#### There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc jupiter.challenges.picoctf.org 44566.

Here we're given a netcat to this link which executes the following code:

````
#include <stdio.h>
#include <stdlib.h>
int main()
{
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int account_balance = 1100;
    while(con == 0){
        
        printf("Welcome to the flag exchange\n");
        printf("We sell flags\n");

        printf("\n1. Check Account Balance\n");
        printf("\n2. Buy Flags\n");
        printf("\n3. Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if(menu == 2){
            printf("Currently for sale\n");
            printf("1. Defintely not the flag Flag\n");
            printf("2. 1337 Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){
                printf("These knockoff Flags cost 900 each, enter desired quantity\n");
                
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }
                                    
                    
                }
                    
                    
                    
                
            }
            else if(auction_choice == 2){
                printf("1337 flags cost 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to buy one");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(account_balance > 100000){
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                        }
                    
                    else{
                        printf("\nNot enough funds for transaction\n\n\n");
                    }}

            }
        }
        else{
            con = 1;
        }

    }
    return 0;
}

````
We see that we get to choose 2 options to buy flags and only if you choose 2 can you get the flag. And to get the flag it requires you to have a bank balance of more than 1000000 by this line 
```
if(account_balance > 100000){
                        FILE *f = fopen("flag.txt", "r");
```

On going through this over and over, the only vulnerability I found was the `total_cost = 900*number_flags;` and `account_balance = account_balance - total_cost;` in option 1. I got stuck here, didn't know what to do so I looked it up :))

On looking up I found out that there's only a maximum amount of integers you can put into an unsigned integer variable which is `2147483647`. 
I divdied this by 900 (price of the flag in option 1 ) to get a value `2386092` I chose a number a few over the value and got this:

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/a81fd532-eb21-4cff-b65c-0af832dab253)

Now that I'm rich, choose option 2 and buy a flag 

![image](https://github.com/slowstabs/CTF-Writeups/assets/148702248/c3a33cbb-2503-4f6f-ad01-594cfcf0ef61)

### Flag: `picoCTF{m0n3y_bag5_68d16363}`
