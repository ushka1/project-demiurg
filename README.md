# Project Demiurg

1. Gra z możliwością przechodzenia między lokacjami.
   Każda lokacja posiada:

   - swój opis,
   - listę przejść do innych lokacji.

   Kreator:

   - twórca za tworzy mapę,
   - twórca ustawia entrance oraz exit (start i koniec gry),
   - twórca eksportuje plik json w odpowiednim formacie,
   - twórca importuje plik json.

   Interpreter:

   - przeszukać folder z grami (bibliotekę), wypisując wszystkie gry,
   - użytkownik wybiera grę,
   - gra zostaje uruchomiona, plik json jest ładowany i na jego podstawie odpalana jest gra.

2.Dodanie interakcji oraz postaci gracza, tworzenia postaci.
3.Dodanie opcji zapisania postępów.
4.Jakiś prosty sposób na udostępnianie gry przez twórcę dla gracza.
5.Refactor i taki tam quality time + sposób dostarczenia (Docker).
