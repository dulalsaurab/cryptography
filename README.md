## Simple Cryptographic Problems 
The solution to these problems are on this git hub repository, I encourage you to complete them yourself before viewing my rough, haphazard, purrrr... code. 

**Problems compiled by Kul Prasad Subedi, The University of Memphis**

#### 1. Decrypt the following encrypted messages using shift cipher 

1.  hjizt5xvi5wz5hvyz5amjh5adiydib5qpgizmvwdgdodzn5viy5rmdodib5zskgjdon 
2. suzawnafy2kgew2ygsd2af2lzw2hjwkwfuw2gx2sf2svnwjksjq2:sulanw2gj2hskkanw; 
3. ftgr3lrlmxfl3tkx3vhggxvmxw3mh3max3bgmxkgxm?3pabva3atl3twoxkltkbxl
4. vobrgvoys.dfchcqczH.sghopzwgv.gvofsr.gsqfsh.ysm.igwbu.dipzwq;ysm.qfmdhcufodvm ography
5. nayknz6hwuanP6pnwjoiep6zwpw6qoejc6odwnaz6oaynap6gau6ajoqna6ykjbezajpehepu6wjz6ejpacnepu 

#### 2.    Write a function that takes integer as input and output corresponding hex value. 
1. e.g. input = (3456729)10 and output = (0x34bed9)16 

#### 3. Write a function that takes hex as input and output corresponding base64 value. 

1. e.g. input = (576974686f75742072616e646f6d6e6573732c2063727970746f67726170687920776f756c6420626520
696d706f737369626c65206265636175736520616c6c206f7065726174696f6e7320776f756c64206265636f6d65207072656469637461626c652c20616e64207468657265666f726520696e7365637572652e)16 

2. and output = V 2l0aG91dCByY W5kb21uZXNzLCBjcnlwdG9 ncmFwaHkgd291bGQgY mUgaW1wb3NzaWJsZSBi ZWNhdXNlIGFsbCBvcGV yY      XRpb25zIHdvdWxkI GJlY 29tZSBwcmV kaWN0Y WJsZSwgY W5kIHRoZX JlZm9yZSBpbnNlY 3V yZS4 = 

#### 4.    Write a function that XOR two strings of the same length. 

1. e.g. str1 = 1c0111001f010100061a024b53535009181c 
     str2 = 686974207468652062756c6c277320657965

#### 5.    The hex encoded string has been XOR’d against a single character. Find the key, decrypt the message. Hint: Devise some method for ”scoring” a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 

1. (3a09060c0705060d1b1b48011b480e071d060c480d1e0 d1a111f 000d1a0d480106480b1a11181c070f 1a091800115248 0106481c000d480f 0d060d1a091c01070648070e481b0d0b1a0 d1c48030d111b44480106480d060b1a11181c010706481b0b00 0d050d1b444809060c480d1e0d06480106481c000d48091c1c0 90b031b480706480b1a11181c071b111b1c0d051b46)16 
