# ЛАБОРАТОРНАЯ РАБОТА №2
## Задача.
Реализовать паттерн "Адаптер" в программе.
## Описание программы
Приложение для простой манипуляции фото. Есть возможность открыть .png или .jpg изображение и провести с ним некоторые манипуляции: отзеркалить вертикально/горизонтально, компрессировать.
## Актуальность паттерна
В рамках используемой библиотеки Pillow изображения можно хранить в двух форматах: как встроенный класс Image, либо закодированными в битовый вектор. Второй метод позволяет передавать изображение другим программам. Используя только первый метод изображение пришлось бы сначала сохранить на диске, и потом считывать с диска другой программой. Однако над закодированным вектором нельзя выполнять встроенные функции библиотеки, они доступны только классу Image.

Паттерн "адаптер" в данном случае идеально подходит для "перевода" функций, чтобы они могли работать как с классом Image, так и с закодированными векторами.
