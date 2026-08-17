{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c27dd358-3195-480d-adc2-c59a8cbb63c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Project 3create a calculator in that shows menu ,perform the selected operation and keep runnning untill user chooses Exit choice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "503dc257-db7a-477b-862a-6a06df75902c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "# **Menu-Driven Calculator 3 project\n"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%%markdown\n",
    "# **Menu-Driven Calculator 3 project"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "501fa5b8-9dd3-4c03-ab7e-066759527e05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=====Menu Driven cCalculator=====\n",
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: 24\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid choice.pleaseselect+,-,*,/,or 0.\n",
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: 32\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid choice.pleaseselect+,-,*,/,or 0.\n",
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: 52\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid choice.pleaseselect+,-,*,/,or 0.\n",
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: *\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: 24\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid choice.pleaseselect+,-,*,/,or 0.\n",
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: /\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: +\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: 24\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid choice.pleaseselect+,-,*,/,or 0.\n",
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: /\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-Subtraction\n",
      "*Multiplication\n",
      "/Division\n",
      "0 Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Calculator closed.\n"
     ]
    }
   ],
   "source": [
    "print(\"=====Menu Driven cCalculator=====\")\n",
    "\n",
    "while True:\n",
    "   print(\"-Subtraction\")\n",
    "   print(\"*Multiplication\")\n",
    "   print(\"/Division\")\n",
    "   print(\"0 Exit\")\n",
    "\n",
    "   choice = input(\"Enter your choice:\")\n",
    "    \n",
    "\n",
    "   if choice==\"0\":\n",
    "      print(\"Calculator closed.\")\n",
    "      break\n",
    "\n",
    "\n",
    "   if choice not in[\"+\",\"-\",\"*\",\"/\"]:\n",
    "      print(\"invalid choice.pleaseselect+,-,*,/,or 0.\")\n",
    "      continue\n",
    "\n",
    "      number1 = float(input(\"Enter first number:\"))\n",
    "      number2 = float(input(\"Enter Second number:\"))\n",
    "\n",
    "    \n",
    "      if choice ==\"+\":\n",
    "         answer = number1 + number2\n",
    "         print(\"Answer:\",answer)\n",
    "\n",
    "      elif choice ==\"-\":\n",
    "           answer = number1 - number2\n",
    "           print(\"Answer:\",answer)\n",
    "\n",
    "      elif choice ==\"*\":\n",
    "           answer = number1 * number2\n",
    "           print(\"Answer:\",answer)\n",
    "\n",
    "      elif choice ==\"/\":\n",
    "        if number2 ==0:\n",
    "           print(\"Division by Zero is not possible.\")\n",
    "        else:\n",
    "          answer = number1/number2\n",
    "          print(\"Answer:\",answer)\n",
    "        \n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f2067d6-c4b7-48a6-a0e8-7110e1b6001f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
