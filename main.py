# cryptic encryption
import krypticfunct as ßkf
import single_char_xor as scxc


def main():
    print('Answer for the first problem')
    shift_ciphers_decoded_text_list = \
        ['hjizt5xvi5wz5hvyz5amjh5adiydib5qpgizmvwdgdodzn5viy5rmdodib5zskgjdon',
         'suzawnafy2kgew2ygsd2af2lzw2hjwkwfuw2gx2sf2svnwjksjq2:sulanw2gj2hskkanw;',
         'ftgr3lrlmxfl3tkx3vhggxvmxw3mh3max3bgmxkgxm?3pabva3atl3twoxkltkbxl',
         'vobrgvoys.dfchcqczH.sghopzwgv.gvofsr.gsqfsh.ysm.igwbu.dipzwq;ysm.qfmdhcufodvm',
         'nayknz6hwuanP6pnwjoiep6zwpw6qoejc6odwnaz6oaynap6gau6ajoqna6ykjbezajpehepu6wjz6ejpacnepu']

    for encoded_text in shift_ciphers_decoded_text_list:
        print(kf.sift_ciphers(encoded_text))
    print("\nAnswer for the second probelem")

    print("Enter your decimal number to convert to hex"+'\n')
    num_to_convert = input()
    try:
        isinstance(int(num_to_convert),int)
        print("You num is " + num_to_convert + " and its corresponding hex value is 0x" + kf.num_to_hex(int(num_to_convert)) +'\n')
    except Exception as e:
        print(num_to_convert+ "is not a valid decimal number \n")

    print('Answer for the third problem')
    hex_string = '''576974686f75742072616e646f6d6e6573732c''' \
                 '2063727970746f67726170687920776f756c6' \
                 '420626520696d706f737369626c6520626563' \
                 '6175736520616c6c206f7065726174696f6e7' \
                 '320776f756c64206265636f6d652070726564' \
                 '69637461626c652c20616e642074686572656' \
                 '66f726520696e7365637572652e'''
    print(kf.base64_encoding(hex_string))

    print('\nAnswer for the forth problem')
    print(kf.XOR('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965','E'))

    print('\nAnswer for the fifth problem')
    encoded = '3a09060c0705060d1b1b48011b480e071d060c480d1e0d1a' \
              '111f000d1a0d480106480b1a11181c070f1a091800115248' \
              '0106481c000d480f0d060d1a091c01070648070e481b0d0b1' \
              'a0d1c48030d111b44480106480d060b1a11181c010706481' \
              'b0b000d050d1b444809060c480d1e0d06480106481c000d4' \
              '8091c1c090b031b480706480b1a11181c071b111b1c0d051b46'''

    print(scxc.__single_char_XOR_cypher(encoded))


if __name__ == '__main__':
    main()
