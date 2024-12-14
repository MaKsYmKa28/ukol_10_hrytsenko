# Refaktorizovaný binární strom

## Autor
**Maksym Hrytsenko**

## Popis projektu
Tento projekt implementuje binární vyhledávací strom s následujícími funkcemi:
1. **Vkládání dat do stromu**: Metoda `insert` umožňuje vložit nové hodnoty do stromu na správné místo.
2. **Hledání hodnoty ve stromu**:
   - Metoda `contains` vyhledává hodnotu v binárním stromu a vrací výsledek ve formátu `(nalezeno, počet kroků)`.
   - Metoda `breadth_first_search` implementuje hledání pomocí BFS (Breadth-First Search).
3. **Výpis stromu**:
   - Metoda `print_tree` vypíše strom jako text s odsazením podle úrovní.
   - Metoda `pretty_print` symetricky vypíše strom tak, aby byla vizualizována jeho struktura.
4. **Zjištění hloubky stromu**: Metoda `max_depth` vypočítá maximální hloubku stromu.

## Změny provedené v kódu
1. **Refaktorizace a optimalizace**:
   - Byly přidány typové anotace (`type hints`), aby byl kód přehlednější a snazší na údržbu.
   - Názvy proměnných a metod byly upraveny podle doporučení PEP8.
   - Duplicita kódu byla odstraněna.

2. **Komentáře v češtině**:
   - Přidány jasné a stručné komentáře v českém jazyce pro lepší porozumění funkcím.

3. **Zajištění souladu s PEP8**:
   - Kód byl upraven dle doporučení PEP8 pro zlepšení čitelnosti a standardizace.

