%{
    const int EXIT_FAIL =-1;
    const int EXIT_OK =0;
    int indicator = 0;
    int line = 0;
    char *addr_type = NULL;
    //
%}
%option noyywrap
%%
. {printf("Error type A at Line %d: Unknown characters \'%s\'\n",yylineno, yytext); }
%%
int main(int argc, char **argv){
    char *file_path;
    if(argc < 2){
        fprintf(stderr, "Usage: %s <file_path>\n", argv[0]);
        return EXIT_FAIL;
    }
    else if(argc == 2){
        file_path = argv[1];
        if(!(yyin = fopen(file_path, "r"))){
            perror(argv[1]);
            return EXIT_FAIL;
        }
        yylex();
        return EXIT_OK;
    }
    else{
        fputs("Too much arguments!\n", stderr);
        return EXIT_FAIL;
    }
}
