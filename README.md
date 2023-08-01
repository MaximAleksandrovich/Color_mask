# Color_mask
Скрипт по проверке наличия элемента на рисунке

Как Вы думаете, сколько цветов на бело-зеленом [логотипе Сбербанка](https://github.com/MaximAleksandrovich/Color_mask/blob/main/part2.png) на иконке в телефоне? На моем скрине 1190 пикселей 525 уникальных цветов (уникальных BGR-кодов). Используя то, что цвета на различных кнопках, иконках и иных частях экрана (далее – на иконках) современных устройств достаточно уникальны, можно определять наличие иконки на скрине экрана по совпадению частот использования пикселей определенного цвета на иконке и на скрине. Надежность определения наличия иконок близка к 100% (в отличие от распознавания иконок по образу), распознание происходит быстро и не требует задействования графического процессора.
[Скрипт](https://github.com/MaximAleksandrovich/Color_mask/blob/main/Mask.py) работает с файлами PNG.
Если искомая картинка не представляет из себя законченного элемента и части картинки выходят за её границы, то вероятность нахождения элемента снижается.
Данный способ плохо подходит для выявления двухцветных элементов с текстом.

