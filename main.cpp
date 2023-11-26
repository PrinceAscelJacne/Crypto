#include <iostream>
#include <string>
using namespace std;

string caesarCipher(string text, int shift) {
    string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (isalpha(text[i])) {
            char base = islower(text[i]) ? 'a' : 'A';
            result += char(int(text[i] - base + shift) % 26 + base);
        } else {
            result += text[i];
        }

    return result;
}

int main() {
    string message;
    int shift;
    cout << "Entrez le message" << endl;
    getline(cin, message);
    cout<< "Entrer le décalage"<<endl;
    getline(cin, shift);
    string encryptedMessage = caesarCipher(message, shift);
    cout << "Message original: " << message << endl;
    cout << "Message code: " << encryptedMessage << endl;
    return 0;
}
