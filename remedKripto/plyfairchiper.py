kunci = input ( "Masukkan kunci" )
kunci = kunci . ganti ( " " , "" )
kunci = kunci . atas ()
 matriks def ( x , y , awal ):
    return [[ inisial  untuk  i  dalam  rentang ( x )] untuk  j  dalam  rentang ( y )]
    
hasil = daftar ()
untuk  kunci c  : #menyimpan  kunci
    jika  c  tidak  dalam  hasil :
        jika  c == 'J' :
            hasil . tambahkan ( 'saya' )
        lain :
            hasil . tambahkan ( c )
bendera = 0
for  i  in  range ( 65 , 91 ): #menyimpan karakter lain
    jika  chr ( i ) tidak  di  hasilkan :
        jika  i == 73  dan  chr ( 74 ) tidak  di  hasilkan :
            hasil . tambahkan ( "saya" )
            bendera = 1
        elif  flag == 0  dan  i == 73  atau  i == 74 :
            lulus    
        lain :
            hasil . tambahkan ( chr ( i ))
k = 0
my_matrix = matriks ( 5 , 5 , 0 ) #inisialisasi matriks
untuk  i  dalam  rentang ( 0 , 5 ): #membuat matriks
    untuk  j  dalam  rentang ( 0 , 5 ):
        my_matrix [ i ][ j ] = hasil [ k ]
        k + = 1

def  locindex ( c ): #dapatkan lokasi setiap karakter
    lokasi = daftar ()
    jika  c == 'J' :
        c = 'aku'
    untuk  i , j  di  enumerate ( my_matrix ):
        untuk  k , l  di  enumerate ( j ):
            jika  c == l :
                lokasi _ tambahkan ( saya )
                lokasi _ tambahkan ( k )
                kembali  ke lokasi
            
def  mengenkripsi ():   #Enkripsi
    msg = str ( masukan ( "MASUKKAN MSG:" ))
    pesan = pesan . atas ()
    pesan = pesan . ganti ( " " , "" )             
    saya = 0
    untuk  s  dalam  rentang ( 0 , len ( msg ) + 1 , 2 ):
        if  s < len ( msg ) - 1 :
            if  msg [ s ] == msg [ s + 1 ]:
                msg = msg [: s + 1 ] + 'X' + msg [ s + 1 :]
    jika  len ( pesan ) % 2 != 0 :
        pesan = pesan [:] + 'X'
    print ( "TEKS CIPHER:" , akhir = ' ' )
    sedangkan  i < len ( msg ):
        lokasi = daftar ()
        loc = locindex ( msg [ i ])
        loc1 = daftar ()
        loc1 = locindex ( msg [ i + 1 ])
        jika  loc [ 1 ] == loc1 [ 1 ]:
            print ( "{}{}" . format ( my_matrix [( loc [ 0 ] + 1 ) % 5 ][ loc [ 1 ]], my_matrix [( loc1 [ 0 ] + 1 ) % 5 ][ loc1 [ 1 ]] ), akhir = ' ' )
        elif  loc [ 0 ] == loc1 [ 0 ]:
            print ( "{}{}" . format ( my_matrix [ loc [ 0 ]][( loc [ 1 ] + 1 ) % 5 ], my_matrix [ loc1 [ 0 ]][( loc1 [ 1 ] + 1 ) % 5 ] ), akhir = ' ' )  
        lain :
            print ( "{}{}" . format ( my_matrix [ loc [ 0 ]][ loc1 [ 1 ]], my_matrix [ loc1 [ 0 ]][ loc [ 1 ]]), end = ' ' )    
        saya = saya + 2        
                 
def  dekripsi ():   #dekripsi
    msg = str ( masukan ( "MASUKKAN TEKS CIPHER:" ))
    pesan = pesan . atas ()
    pesan = pesan . ganti ( " " , "" )
    print ( "TEKS POLOS:" , akhir = ' ' )
    saya = 0
    sedangkan  i < len ( msg ):
        lokasi = daftar ()
        loc = locindex ( msg [ i ])
        loc1 = daftar ()
        loc1 = locindex ( msg [ i + 1 ])
        jika  loc [ 1 ] == loc1 [ 1 ]:
            print ( "{}{}" . format ( my_matrix [( loc [ 0 ] - 1 ) % 5 ][ loc [ 1 ]], my_matrix [( loc1 [ 0 ] - 1 ) % 5 ][ loc1 [ 1 ]] ), akhir = ' ' )
        elif  loc [ 0 ] == loc1 [ 0 ]:
            print ( "{}{}" . format ( my_matrix [ loc [ 0 ]][( loc [ 1 ] - 1 ) % 5 ], my_matrix [ loc1 [ 0 ]][( loc1 [ 1 ] - 1 ) % 5 ] ), akhir = ' ' )  
        lain :
            print ( "{}{}" . format ( my_matrix [ loc [ 0 ]][ loc1 [ 1 ]], my_matrix [ loc1 [ 0 ]][ loc [ 1 ]]), end = ' ' )    
        saya = saya + 2        

sedangkan ( 1 ):
    pilihan = int ( input ( " \n 1.Enkripsi \n 2.Dekripsi: \n 3.EXIT" ))
    jika  pilihan == 1 :
        mengenkripsi ()
     pilihan elif == 2 :
        mendekripsi ()
     pilihan elif == 3 :
        keluar ()
    lain :
        print ( "Pilih pilihan yang benar" )