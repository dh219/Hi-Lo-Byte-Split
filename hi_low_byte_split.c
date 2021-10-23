#include <stdlib.h>
#include <stdio.h>

int main( int argc, char *argv[] ) {

  if( argc < 4 ) {
    fprintf( stderr, "Usage: %s <input_rom_image> <output_file_high> <output_file_low>\n", argv[0]);
    return 1;
  }

  FILE *fp = fopen( argv[1], "rb" );
  if( !fp ) {
    fprintf( stderr, "Couldn't open '%s' for read\n", argv[1]);
    return 2;
  }
  FILE *fph = fopen( argv[2], "wb" );
  if( !fph ) {
    fprintf( stderr, "Couldn't open '%s' for write\n", argv[2]);
    return 3;
  }
  FILE *fpl = fopen( argv[3], "wb" );
  if( !fpl ) {
    fprintf( stderr, "Couldn't open '%s' for write\n", argv[3]);
    return 4;
  }
    

  long offset = 0L;
  int  byte;
  while( ( byte = fgetc(fp) ) != EOF ) {
    if( offset % 2 == 0)
      fputc( byte, fph );
    else
      fputc( byte, fpl);
    offset++;
  }
  printf("%ld bytes read\n", offset );

  fclose(fp);
  fclose(fph);
  fclose(fpl);

  return 0;
}