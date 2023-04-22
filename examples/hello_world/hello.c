/* YAMLScan (Hello World Example)
 * A tool for scanning files and
 * Github: https//www.github.com/awesomelewis2007/YAMLscan
 * Licence: GPL-3.0
 * By: Lewis Evans
 *
 * C Hello World Example for YAMLscan
 *
 * Compile this program with gcc and run 
 * it with YAMLscan.
 * 
 * gcc -o hello hello.c
 * python3 -m yamlscan hello rule.yaml
 * 
 * It should print flag Hello world! and 
 * the printf functions in the file
*/

#include "stdio.h"

int main(int argc, char **argv) {
    printf("Hello world!");
    return 0;
}