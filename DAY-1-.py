{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "77a0a94d-cf8b-46d2-be23-b62cab791cae",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "64347ea9-d3a6-4115-9d89-2ee455929eee",
   "metadata": {},
   "outputs": [],
   "source": [
    "name=['a','b','c','d','e']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "6a9e33dc-976b-4792-91b2-2b5704ddf620",
   "metadata": {},
   "outputs": [],
   "source": [
    "id=[1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "6f8a3f1a-4c43-47ff-9f2a-f8a146605396",
   "metadata": {},
   "outputs": [],
   "source": [
    "salary=[1000,2000,3000,4000,5000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "da686aa1-3163-42fe-a0f3-69ec9e9cc5e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame({\"name\":name,\"emp_id\":id,\"salary\":salary})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "93718f3d-29ca-43b8-8051-940261c20f40",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>emp_id</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>1</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>2</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>3</td>\n",
       "      <td>3000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>4</td>\n",
       "      <td>4000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e</td>\n",
       "      <td>5</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  name  emp_id  salary\n",
       "0    a       1    1000\n",
       "1    b       2    2000\n",
       "2    c       3    3000\n",
       "3    d       4    4000\n",
       "4    e       5    5000"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "1afdcc6c-d860-4c1f-b57d-bf0121ab6586",
   "metadata": {},
   "outputs": [],
   "source": [
    "#numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "e688fa6c-ca9b-4c9b-9c59-3df85f2327df",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "040d3c94-080c-482d-92a5-0f402e198365",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20])"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(1,21)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "6e745080-e50f-4c7a-b56c-89a4ad7f7542",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 2,  4,  6,  8, 10, 12, 14, 16, 18, 20])"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(2,22,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "44bf3783-21df-4119-b1f1-1e8cf963eeff",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[3,4,5,6]\n",
    "d1=np.array(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "adf9d1e0-83d0-4ab8-9020-060480b0a91a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 4, 5, 6])"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "fa61a381-6671-4741-99a6-09e7506133ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.ndim(d1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "913a2fe6-2ff6-499e-bc2f-abd5ade84286",
   "metadata": {},
   "outputs": [],
   "source": [
    "d2=[[1,2,3],[4,5,6]]\n",
    "d2=np.array(d2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "dfbfadcd-ca03-4cc4-a2e1-d8837de37792",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6]])"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "82c55222-c633-420a-b82d-ce5f830d85ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.ndim(d2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "61eb9a80-c0b4-4230-9ff4-6ac733a0ab29",
   "metadata": {},
   "outputs": [],
   "source": [
    "l=[[1,2,3]],[[4,5,6]],[[7,8,9]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "f0ef7e91-3e54-4854-b5cb-3e0e93eb2909",
   "metadata": {},
   "outputs": [],
   "source": [
    "d3=np.array(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "f848b84c-4847-4a6c-ab65-99cb56b7ca7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1, 2, 3]],\n",
       "\n",
       "       [[4, 5, 6]],\n",
       "\n",
       "       [[7, 8, 9]]])"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "5e9ad3d3-359e-4783-aec0-1c5cad09c3b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.ndim(d3)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "6f3a4409-07da-45a2-983d-4c4322d58ce2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(len(d3))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e02f53f-ff0f-49e3-b3e6-eb9d1ebf1cfa",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true
   },
   "source": [
    "d3.reshape(3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "4296cfab-384c-4d62-a26b-f93c1f049d05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d3.ravel()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "20652d8c-cfbd-4a1d-a352-14d7cdd457a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>emp_id</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>1</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>2</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>3</td>\n",
       "      <td>3000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>4</td>\n",
       "      <td>4000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e</td>\n",
       "      <td>5</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  name  emp_id  salary\n",
       "0    a       1    1000\n",
       "1    b       2    2000\n",
       "2    c       3    3000\n",
       "3    d       4    4000\n",
       "4    e       5    5000"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "474074bc-a2e0-460b-9dbd-d42534e258f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10],\n",
       "       [11, 12, 13, 14, 15],\n",
       "       [16, 17, 18, 19, 20]])"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=np.arange(1,21).reshape(4,5)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "dc5b0794-6970-4355-9629-aeab602425ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1=pd.DataFrame(data=df,index=[\"row1\",\"row2\",\"row3\",\"row4\"],columns=[\"C1\",\"C2\",\"C3\",\"C4\",\"C5\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "01f9a60b-6f78-4111-b819-5756743913e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10],\n",
       "       [11, 12, 13, 14, 15],\n",
       "       [16, 17, 18, 19, 20]])"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "9c6de802-c050-4e74-9da0-fc41d3c9c604",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row4</th>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "      <td>18</td>\n",
       "      <td>19</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row1   1   2   3   4   5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15\n",
       "row4  16  17  18  19  20"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "d6f429e5-f7a7-441c-aab7-d65ad18ed9f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "abc = pd.read_csv(\"data.csv\", encoding=\"latin1\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "id": "668ef400-4473-4c19-ac53-ba5ae71d09b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Table_Tau</th>\n",
       "      <th>Table_name</th>\n",
       "      <th>Table_sub_name</th>\n",
       "      <th>Breakdown</th>\n",
       "      <th>Section</th>\n",
       "      <th>Units</th>\n",
       "      <th>Value</th>\n",
       "      <th>Time_Period</th>\n",
       "      <th>Footnotes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>58656</td>\n",
       "      <td>2012</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>56538</td>\n",
       "      <td>2013</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>56514</td>\n",
       "      <td>2014</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>57174</td>\n",
       "      <td>2015</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>56592</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2879</th>\n",
       "      <td>Ripanga 23</td>\n",
       "      <td>Nga raraunga whakawhiwhi mahi umanga nga tura...</td>\n",
       "      <td>Ma te momo umanga</td>\n",
       "      <td>Tapeke whiwhinga moni</td>\n",
       "      <td>Nga uepu Maori</td>\n",
       "      <td>$(miriona)</td>\n",
       "      <td>173</td>\n",
       "      <td>2020_03</td>\n",
       "      <td>1 me 2 me 3 me 4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2880</th>\n",
       "      <td>Ripanga 23</td>\n",
       "      <td>Nga raraunga whakawhiwhi mahi umanga nga tura...</td>\n",
       "      <td>Ma te momo umanga</td>\n",
       "      <td>Tapeke whiwhinga moni</td>\n",
       "      <td>Nga uepu Maori</td>\n",
       "      <td>$(miriona)</td>\n",
       "      <td>182</td>\n",
       "      <td>2020_06</td>\n",
       "      <td>1 me 2 me 3 me 4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2881</th>\n",
       "      <td>Ripanga 23</td>\n",
       "      <td>Nga raraunga whakawhiwhi mahi umanga nga tura...</td>\n",
       "      <td>Ma te momo umanga</td>\n",
       "      <td>Tapeke whiwhinga moni</td>\n",
       "      <td>Nga uepu Maori</td>\n",
       "      <td>$(miriona)</td>\n",
       "      <td>182</td>\n",
       "      <td>2020_09</td>\n",
       "      <td>1 me 2 me 3 me 4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2882</th>\n",
       "      <td>Ripanga 23</td>\n",
       "      <td>Nga raraunga whakawhiwhi mahi umanga nga tura...</td>\n",
       "      <td>Ma te momo umanga</td>\n",
       "      <td>Tapeke whiwhinga moni</td>\n",
       "      <td>Nga uepu Maori</td>\n",
       "      <td>$(miriona)</td>\n",
       "      <td>188</td>\n",
       "      <td>2020_12</td>\n",
       "      <td>1 me 2 me 3 me 4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2883</th>\n",
       "      <td>Ripanga 23</td>\n",
       "      <td>Nga raraunga whakawhiwhi mahi umanga nga tura...</td>\n",
       "      <td>Ma te momo umanga</td>\n",
       "      <td>Tapeke whiwhinga moni</td>\n",
       "      <td>Nga uepu Maori</td>\n",
       "      <td>$(miriona)</td>\n",
       "      <td>180</td>\n",
       "      <td>2021_03</td>\n",
       "      <td>1 me 2 me 3 me 4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2884 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Table_Tau                                         Table_name  \\\n",
       "0      Ripanga 1        Te tatauranga o nga umanga  Nga uepu Maori   \n",
       "1      Ripanga 1        Te tatauranga o nga umanga  Nga uepu Maori   \n",
       "2      Ripanga 1        Te tatauranga o nga umanga  Nga uepu Maori   \n",
       "3      Ripanga 1        Te tatauranga o nga umanga  Nga uepu Maori   \n",
       "4      Ripanga 1        Te tatauranga o nga umanga  Nga uepu Maori   \n",
       "...          ...                                                ...   \n",
       "2879  Ripanga 23  Nga raraunga whakawhiwhi mahi umanga nga tura...   \n",
       "2880  Ripanga 23  Nga raraunga whakawhiwhi mahi umanga nga tura...   \n",
       "2881  Ripanga 23  Nga raraunga whakawhiwhi mahi umanga nga tura...   \n",
       "2882  Ripanga 23  Nga raraunga whakawhiwhi mahi umanga nga tura...   \n",
       "2883  Ripanga 23  Nga raraunga whakawhiwhi mahi umanga nga tura...   \n",
       "\n",
       "         Table_sub_name              Breakdown                      Section  \\\n",
       "0     A-wehenga ahumahi              Ahuwhenua  Nga umanga katoa o Aotearoa   \n",
       "1     A-wehenga ahumahi              Ahuwhenua  Nga umanga katoa o Aotearoa   \n",
       "2     A-wehenga ahumahi              Ahuwhenua  Nga umanga katoa o Aotearoa   \n",
       "3     A-wehenga ahumahi              Ahuwhenua  Nga umanga katoa o Aotearoa   \n",
       "4     A-wehenga ahumahi              Ahuwhenua  Nga umanga katoa o Aotearoa   \n",
       "...                 ...                    ...                          ...   \n",
       "2879  Ma te momo umanga  Tapeke whiwhinga moni               Nga uepu Maori   \n",
       "2880  Ma te momo umanga  Tapeke whiwhinga moni               Nga uepu Maori   \n",
       "2881  Ma te momo umanga  Tapeke whiwhinga moni               Nga uepu Maori   \n",
       "2882  Ma te momo umanga  Tapeke whiwhinga moni               Nga uepu Maori   \n",
       "2883  Ma te momo umanga  Tapeke whiwhinga moni               Nga uepu Maori   \n",
       "\n",
       "                           Units  Value Time_Period         Footnotes  \n",
       "0     Te tatauranga o nga umanga  58656        2012                 1  \n",
       "1     Te tatauranga o nga umanga  56538        2013                 1  \n",
       "2     Te tatauranga o nga umanga  56514        2014                 1  \n",
       "3     Te tatauranga o nga umanga  57174        2015                 1  \n",
       "4     Te tatauranga o nga umanga  56592        2016                 1  \n",
       "...                          ...    ...         ...               ...  \n",
       "2879                  $(miriona)    173     2020_03  1 me 2 me 3 me 4  \n",
       "2880                  $(miriona)    182     2020_06  1 me 2 me 3 me 4  \n",
       "2881                  $(miriona)    182     2020_09  1 me 2 me 3 me 4  \n",
       "2882                  $(miriona)    188     2020_12  1 me 2 me 3 me 4  \n",
       "2883                  $(miriona)    180     2021_03  1 me 2 me 3 me 4  \n",
       "\n",
       "[2884 rows x 9 columns]"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "id": "56def384-7ea4-4bdb-83dc-d6d1a72c63db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Table_Tau</th>\n",
       "      <th>Table_name</th>\n",
       "      <th>Table_sub_name</th>\n",
       "      <th>Breakdown</th>\n",
       "      <th>Section</th>\n",
       "      <th>Units</th>\n",
       "      <th>Value</th>\n",
       "      <th>Time_Period</th>\n",
       "      <th>Footnotes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>58656</td>\n",
       "      <td>2012</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>56538</td>\n",
       "      <td>2013</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>56514</td>\n",
       "      <td>2014</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>57174</td>\n",
       "      <td>2015</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ripanga 1</td>\n",
       "      <td>Te tatauranga o nga umanga  Nga uepu Maori</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>Ahuwhenua</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>Te tatauranga o nga umanga</td>\n",
       "      <td>56592</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Table_Tau                                   Table_name     Table_sub_name  \\\n",
       "0  Ripanga 1  Te tatauranga o nga umanga  Nga uepu Maori  A-wehenga ahumahi   \n",
       "1  Ripanga 1  Te tatauranga o nga umanga  Nga uepu Maori  A-wehenga ahumahi   \n",
       "2  Ripanga 1  Te tatauranga o nga umanga  Nga uepu Maori  A-wehenga ahumahi   \n",
       "3  Ripanga 1  Te tatauranga o nga umanga  Nga uepu Maori  A-wehenga ahumahi   \n",
       "4  Ripanga 1  Te tatauranga o nga umanga  Nga uepu Maori  A-wehenga ahumahi   \n",
       "\n",
       "   Breakdown                      Section                       Units  Value  \\\n",
       "0  Ahuwhenua  Nga umanga katoa o Aotearoa  Te tatauranga o nga umanga  58656   \n",
       "1  Ahuwhenua  Nga umanga katoa o Aotearoa  Te tatauranga o nga umanga  56538   \n",
       "2  Ahuwhenua  Nga umanga katoa o Aotearoa  Te tatauranga o nga umanga  56514   \n",
       "3  Ahuwhenua  Nga umanga katoa o Aotearoa  Te tatauranga o nga umanga  57174   \n",
       "4  Ahuwhenua  Nga umanga katoa o Aotearoa  Te tatauranga o nga umanga  56592   \n",
       "\n",
       "  Time_Period Footnotes  \n",
       "0        2012         1  \n",
       "1        2013         1  \n",
       "2        2014         1  \n",
       "3        2015         1  \n",
       "4        2016         1  "
      ]
     },
     "execution_count": 172,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "8e3a492f-5215-4484-87a9-90f809c8d2e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Table_Tau</th>\n",
       "      <th>Table_name</th>\n",
       "      <th>Table_sub_name</th>\n",
       "      <th>Breakdown</th>\n",
       "      <th>Section</th>\n",
       "      <th>Units</th>\n",
       "      <th>Value</th>\n",
       "      <th>Time_Period</th>\n",
       "      <th>Footnotes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "      <td>2884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>23</td>\n",
       "      <td>23</td>\n",
       "      <td>10</td>\n",
       "      <td>130</td>\n",
       "      <td>13</td>\n",
       "      <td>20</td>\n",
       "      <td>1805</td>\n",
       "      <td>52</td>\n",
       "      <td>39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>Ripanga 3</td>\n",
       "      <td>Tatauranga o nga umanga  umanga iti, wawaenga...</td>\n",
       "      <td>A-wehenga ahumahi</td>\n",
       "      <td>-</td>\n",
       "      <td>Nga umanga katoa o Aotearoa</td>\n",
       "      <td>$(mano)</td>\n",
       "      <td>15</td>\n",
       "      <td>2020</td>\n",
       "      <td>1 me 2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>423</td>\n",
       "      <td>423</td>\n",
       "      <td>936</td>\n",
       "      <td>221</td>\n",
       "      <td>729</td>\n",
       "      <td>558</td>\n",
       "      <td>43</td>\n",
       "      <td>386</td>\n",
       "      <td>633</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Table_Tau                                         Table_name  \\\n",
       "count        2884                                               2884   \n",
       "unique         23                                                 23   \n",
       "top     Ripanga 3  Tatauranga o nga umanga  umanga iti, wawaenga...   \n",
       "freq          423                                                423   \n",
       "\n",
       "           Table_sub_name Breakdown                      Section    Units  \\\n",
       "count                2884      2884                         2884     2884   \n",
       "unique                 10       130                           13       20   \n",
       "top     A-wehenga ahumahi         -  Nga umanga katoa o Aotearoa  $(mano)   \n",
       "freq                  936       221                          729      558   \n",
       "\n",
       "       Value Time_Period Footnotes  \n",
       "count   2884        2884      2884  \n",
       "unique  1805          52        39  \n",
       "top       15        2020    1 me 2  \n",
       "freq      43         386       633  "
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "ea7926b3-7e56-41f2-8cb0-44c704910671",
   "metadata": {},
   "outputs": [],
   "source": [
    "a1=['a','b','c','d','e']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "id": "3fd15795-6b03-450d-bca1-20986f3a69e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "a2=[1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a12e9cad-4445-4597-888e-a708747b6edb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "fbf5a498-4587-4d8b-875b-93ac545c7fcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Username a\n"
     ]
    }
   ],
   "source": [
    "username=input(\"Enter Username\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d638b9e6-b56f-440c-95fe-15a52c7c721e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "6041fd1b-2272-4934-ab58-b916373ac9e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter password 1\n"
     ]
    }
   ],
   "source": [
    "password=input(\"Enter password\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "c24d5f32-3aaa-47af-a2f0-a298a3eb680a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "root=tk.Tk()\n",
    "def main(): #function \n",
    "    root.title(\"my app\")\n",
    "    root.geometry(\"300x400\")\n",
    "    tk.Label(root,text='PIET College').pack()\n",
    "    L1=tk.Label(root,text=\"Username\").place(x=40,y=60)\n",
    "    L2=tk.Label(root,text=\"Password\").place(x=40,y=100)\n",
    "    e1=tk.Entry(root)\n",
    "    e1.place(x=100,y=60)\n",
    "    e2=tk.Entry(root)\n",
    "    e2.place(x=100,y=100)\n",
    "    b1=tk.Button(root,text=\"SUBMIT\",bg=\"green\",command=show).place(x=130,y=150)\n",
    "    b2=tk.Button(root,text=\"SIGNUP\",bg=\"green\",command=show1).place(x=130,y=190)\n",
    "    \n",
    "    root.mainloop()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "73ef4d31-2ce5-4c6a-8ff3-94f76bd3e42a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def show():\n",
    "    root=tk.Tk()\n",
    "    root.config(bg=\"yellow\")\n",
    "    root.geometry(\"200x200\")\n",
    "    tk.Label(root,text=\"LOGIN\").pack()\n",
    "    root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "6a9379ab-9d87-4410-acc0-6a289445b8a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def show1():\n",
    "    root=tk.Tk()\n",
    "    root.config(bg=\"red\")\n",
    "    root.geometry(\"300x200\")\n",
    "    tk.Label(root,text=\"SIGNUP\").pack()\n",
    "    L1=tk.Label(root,text=\"FIRST NAME\").place(x=40,y=60)\n",
    "    L2=tk.Label(root,text=\"LAST NAME\").place(x=40,y=100)\n",
    "    e1=tk.Entry(root)\n",
    "    e1.place(x=100,y=60)\n",
    "    e2=tk.Entry(root)\n",
    "    e2.place(x=100,y=100)\n",
    "    root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "10f7cf14-8bc7-4a38-a991-41337b42d391",
   "metadata": {},
   "outputs": [],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "7fc1ac80-a35b-424c-8770-7e99e9f10f85",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#PANDAS OPERATIONS\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "a3593fbf-54fd-47ed-ae00-baa0c9490ec7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4, 5)"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "id": "08124a29-ada2-4a5e-aaaa-62bf3045398c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row4</th>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "      <td>18</td>\n",
       "      <td>19</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row1   1   2   3   4   5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15\n",
       "row4  16  17  18  19  20"
      ]
     },
     "execution_count": 232,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "id": "dfed8599-75fc-4c38-918f-fe44072c7090",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row4</th>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "      <td>18</td>\n",
       "      <td>19</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row1   1   2   3   4   5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15\n",
       "row4  16  17  18  19  20"
      ]
     },
     "execution_count": 234,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "a55c1656-efab-4c45-8c69-6df57588888d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>8.500000</td>\n",
       "      <td>9.500000</td>\n",
       "      <td>10.500000</td>\n",
       "      <td>11.500000</td>\n",
       "      <td>12.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6.454972</td>\n",
       "      <td>6.454972</td>\n",
       "      <td>6.454972</td>\n",
       "      <td>6.454972</td>\n",
       "      <td>6.454972</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.750000</td>\n",
       "      <td>5.750000</td>\n",
       "      <td>6.750000</td>\n",
       "      <td>7.750000</td>\n",
       "      <td>8.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>8.500000</td>\n",
       "      <td>9.500000</td>\n",
       "      <td>10.500000</td>\n",
       "      <td>11.500000</td>\n",
       "      <td>12.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>12.250000</td>\n",
       "      <td>13.250000</td>\n",
       "      <td>14.250000</td>\n",
       "      <td>15.250000</td>\n",
       "      <td>16.250000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>16.000000</td>\n",
       "      <td>17.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              C1         C2         C3         C4         C5\n",
       "count   4.000000   4.000000   4.000000   4.000000   4.000000\n",
       "mean    8.500000   9.500000  10.500000  11.500000  12.500000\n",
       "std     6.454972   6.454972   6.454972   6.454972   6.454972\n",
       "min     1.000000   2.000000   3.000000   4.000000   5.000000\n",
       "25%     4.750000   5.750000   6.750000   7.750000   8.750000\n",
       "50%     8.500000   9.500000  10.500000  11.500000  12.500000\n",
       "75%    12.250000  13.250000  14.250000  15.250000  16.250000\n",
       "max    16.000000  17.000000  18.000000  19.000000  20.000000"
      ]
     },
     "execution_count": 236,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "id": "0911f5e3-fb2d-4126-92a2-a47a7788f210",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 4 entries, row1 to row4\n",
      "Data columns (total 5 columns):\n",
      " #   Column  Non-Null Count  Dtype\n",
      "---  ------  --------------  -----\n",
      " 0   C1      4 non-null      int64\n",
      " 1   C2      4 non-null      int64\n",
      " 2   C3      4 non-null      int64\n",
      " 3   C4      4 non-null      int64\n",
      " 4   C5      4 non-null      int64\n",
      "dtypes: int64(5)\n",
      "memory usage: 192.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "df1.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "id": "55119727-4a10-4c04-b74e-86818e968499",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row4</th>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "      <td>18</td>\n",
       "      <td>19</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row1   1   2   3   4   5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15\n",
       "row4  16  17  18  19  20"
      ]
     },
     "execution_count": 240,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "f424f95f-c76f-4521-a266-c58d84a164ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "row1     2\n",
       "row2     7\n",
       "row3    12\n",
       "row4    17\n",
       "Name: C2, dtype: int64"
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#to EXTRACT a column\n",
    "df1.C2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "a4f2b03e-8648-499b-aa6f-f2a21ff9eac3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "row1     1\n",
       "row2     6\n",
       "row3    11\n",
       "row4    16\n",
       "Name: C1, dtype: int64"
      ]
     },
     "execution_count": 244,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#to EXTRACT a column\n",
    "df1[\"C1\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "id": "49e26a02-3890-4222-be41-bd6beee5ae1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row4</th>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2\n",
       "row1   1   2\n",
       "row2   6   7\n",
       "row3  11  12\n",
       "row4  16  17"
      ]
     },
     "execution_count": 257,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#TO EXTRACT MULTIPLE COLUMN\n",
    "df1[[\"C1\",\"C2\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "id": "05d0eb32-3693-45fe-9254-ed01feb7ceeb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row4</th>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "      <td>18</td>\n",
       "      <td>19</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15\n",
       "row4  16  17  18  19  20"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#CONDITIONAL OPERATIONS WITH THE HELP OF PANDAS\n",
    "df1[df1[\"C2\"]>2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 277,
   "id": "26128476-7013-4505-96fd-46c79f7394b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15"
      ]
     },
     "execution_count": 277,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#writE EQN TO EXTRACT THE DATA FROM DF1  WHERE COLUMN 2  IS GREATER THAN TWO AND LESS THAN 17\n",
    "df1[(df1[\"C2\"] > 2) & (df1[\"C2\"] < 17)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "id": "75bca682-18e7-4a8b-b087-3e1e00558091",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10],\n",
       "       [11, 12, 13, 14, 15],\n",
       "       [16, 17, 18, 19, 20]])"
      ]
     },
     "execution_count": 279,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "id": "64d89dc2-18cf-466e-be7b-175cd6b77b0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row4</th>\n",
       "      <td>16</td>\n",
       "      <td>17</td>\n",
       "      <td>18</td>\n",
       "      <td>19</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row1   1   2   3   4   5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15\n",
       "row4  16  17  18  19  20"
      ]
     },
     "execution_count": 281,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "id": "f00615cc-e619-407a-bac2-e1ade3e52790",
   "metadata": {},
   "outputs": [],
   "source": [
    "name=['a','b','c','d','e']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "id": "215f13de-4b10-410d-bc34-04e85aefd1a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "id=[1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 288,
   "id": "f0b4202a-8cd9-4fc1-83dc-ba2fa1716488",
   "metadata": {},
   "outputs": [],
   "source": [
    "salary=[1000,2000,3000,4000,5000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 290,
   "id": "e5fe5944-a534-438d-843d-d33851d80cd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame({\"name\":name,\"emp_id\":id,\"salary\":salary})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 292,
   "id": "2414a374-fa05-4c5c-8998-4048c3de12f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>emp_id</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>1</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>2</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>3</td>\n",
       "      <td>3000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>4</td>\n",
       "      <td>4000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e</td>\n",
       "      <td>5</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  name  emp_id  salary\n",
       "0    a       1    1000\n",
       "1    b       2    2000\n",
       "2    c       3    3000\n",
       "3    d       4    4000\n",
       "4    e       5    5000"
      ]
     },
     "execution_count": 292,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 294,
   "id": "8e7495ed-4512-40ca-b00a-68cf2db529dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C1</th>\n",
       "      <th>C2</th>\n",
       "      <th>C3</th>\n",
       "      <th>C4</th>\n",
       "      <th>C5</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>row2</th>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>row3</th>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      C1  C2  C3  C4  C5\n",
       "row2   6   7   8   9  10\n",
       "row3  11  12  13  14  15"
      ]
     },
     "execution_count": 294,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.loc[[\"row2\",\"row3\"]] #data extract"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "id": "bb6e566d-bc18-4524-962e-be5df4c1b41f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>emp_id</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>3</td>\n",
       "      <td>3000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>4</td>\n",
       "      <td>4000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  name  emp_id  salary\n",
       "2    c       3    3000\n",
       "3    d       4    4000"
      ]
     },
     "execution_count": 300,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[[2,3]] #data extract\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 306,
   "id": "c0f824e5-57c9-43d7-81a8-5d7aced32d69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 306,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.iloc[1,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 310,
   "id": "a1f2251d-319a-48c5-9827-42834699b907",
   "metadata": {},
   "outputs": [],
   "source": [
    "#add s new column in the existing dataset \n",
    "df[\"designation\"] = [\"hr\",\"sde\",\"da\",\"ds\",\"intern\"]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "id": "9b1fe4d5-adf9-47cb-b8df-46f601bbb552",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>emp_id</th>\n",
       "      <th>salary</th>\n",
       "      <th>designation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>1</td>\n",
       "      <td>1000</td>\n",
       "      <td>hr</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>2</td>\n",
       "      <td>2000</td>\n",
       "      <td>sde</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>3</td>\n",
       "      <td>3000</td>\n",
       "      <td>da</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>4</td>\n",
       "      <td>4000</td>\n",
       "      <td>ds</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e</td>\n",
       "      <td>5</td>\n",
       "      <td>5000</td>\n",
       "      <td>intern</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  name  emp_id  salary designation\n",
       "0    a       1    1000          hr\n",
       "1    b       2    2000         sde\n",
       "2    c       3    3000          da\n",
       "3    d       4    4000          ds\n",
       "4    e       5    5000      intern"
      ]
     },
     "execution_count": 312,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 314,
   "id": "08de1f46-ed72-418a-aab5-e173f18e1283",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"incentive\"]=(df.salary)*0.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
   "id": "51856c16-7e31-43e9-8012-9be5f3ee48e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>emp_id</th>\n",
       "      <th>salary</th>\n",
       "      <th>designation</th>\n",
       "      <th>incentive</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>1</td>\n",
       "      <td>1000</td>\n",
       "      <td>hr</td>\n",
       "      <td>100.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>2</td>\n",
       "      <td>2000</td>\n",
       "      <td>sde</td>\n",
       "      <td>200.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>3</td>\n",
       "      <td>3000</td>\n",
       "      <td>da</td>\n",
       "      <td>300.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>4</td>\n",
       "      <td>4000</td>\n",
       "      <td>ds</td>\n",
       "      <td>400.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e</td>\n",
       "      <td>5</td>\n",
       "      <td>5000</td>\n",
       "      <td>intern</td>\n",
       "      <td>500.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  name  emp_id  salary designation  incentive\n",
       "0    a       1    1000          hr      100.0\n",
       "1    b       2    2000         sde      200.0\n",
       "2    c       3    3000          da      300.0\n",
       "3    d       4    4000          ds      400.0\n",
       "4    e       5    5000      intern      500.0"
      ]
     },
     "execution_count": 316,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "id": "53f3b995-9d35-41b1-afd0-ef0ea75e3cdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "rank=[1,2,3,4,5,6,7,8,9,10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 322,
   "id": "798fff28-1b22-44cd-b73a-acef03c7235b",
   "metadata": {},
   "outputs": [],
   "source": [
    "name=[\"V KOHLI\",\"S DHAWAN\",\"ROHIT SHARMA\",\"SURESH RAINA\",\"DAVID WARNER\",\"AB DE WILLIAMS\",\"CHRIS GAYLE\",\"MS DHONI\",\"ROBIN UTHAPPA\",\"GAUTAM GAMBHIR\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 324,
   "id": "9759aa09-6b7d-4cf0-a2cf-da3939594ff8",
   "metadata": {},
   "outputs": [],
   "source": [
    "matches=[207,194,213,205,150,184,142,220,193,154]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 328,
   "id": "08819f0a-af71-48c0-803b-41c17ef5d197",
   "metadata": {},
   "outputs": [],
   "source": [
    "innings=[199,191,208,200,150,170,141,193,186,152]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "id": "160d244b-4ee5-4c7a-b71d-f893b79cac65",
   "metadata": {},
   "outputs": [],
   "source": [
    "runs=[6283,5784,5611,5528,5449,5162,4965,4746,4722,4217]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 344,
   "id": "845b132e-fb07-47e4-bef0-0d7446270f4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "highest=[113,106,109,100,126,133,175,84,87,93]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "id": "bc9d7dbd-8d36-4cc9-b559-5242f468fcf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "hundreds=[5,2,1,1,4,3,6,0,0,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "id": "5d51c31c-3369-4a9f-b60b-e996ac4e7be9",
   "metadata": {},
   "outputs": [],
   "source": [
    "fifties=[42,44,40,39,50,40,31,23,25,36]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 356,
   "id": "3158af2e-3fd1-420a-962d-ef7f412736f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.DataFrame({\"rank\":rank,\"name\":name,\"matches\":matches,\"innings\":innings,\"runs\":runs,\"highest\":highest,\"hundreds\":hundreds,\"fifties\":fifties})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 358,
   "id": "2f291b93-c2eb-446b-9a8f-0b3ff2563132",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rank</th>\n",
       "      <th>name</th>\n",
       "      <th>matches</th>\n",
       "      <th>innings</th>\n",
       "      <th>runs</th>\n",
       "      <th>highest</th>\n",
       "      <th>hundreds</th>\n",
       "      <th>fifties</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>V KOHLI</td>\n",
       "      <td>207</td>\n",
       "      <td>199</td>\n",
       "      <td>6283</td>\n",
       "      <td>113</td>\n",
       "      <td>5</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>S DHAWAN</td>\n",
       "      <td>194</td>\n",
       "      <td>191</td>\n",
       "      <td>5784</td>\n",
       "      <td>106</td>\n",
       "      <td>2</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>AB DE WILLIAMS</td>\n",
       "      <td>184</td>\n",
       "      <td>170</td>\n",
       "      <td>5162</td>\n",
       "      <td>133</td>\n",
       "      <td>3</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   rank            name  matches  innings  runs  highest  hundreds  fifties\n",
       "0     1         V KOHLI      207      199  6283      113         5       42\n",
       "1     2        S DHAWAN      194      191  5784      106         2       44\n",
       "5     6  AB DE WILLIAMS      184      170  5162      133         3       40"
      ]
     },
     "execution_count": 358,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[(data[\"innings\"]>150) & (data[\"hundreds\"]>=2) & (data[\"fifties\"]>=35)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 370,
   "id": "bd780e23-820e-4d05-9990-3c92c5620d96",
   "metadata": {},
   "outputs": [],
   "source": [
    "data[\"bowl\"] = data[\"matches\"] - data[\"innings\"]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 372,
   "id": "0d4e56a4-e2a1-4fb0-9b60-ba7963d3db6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rank</th>\n",
       "      <th>name</th>\n",
       "      <th>matches</th>\n",
       "      <th>innings</th>\n",
       "      <th>runs</th>\n",
       "      <th>highest</th>\n",
       "      <th>hundreds</th>\n",
       "      <th>fifties</th>\n",
       "      <th>bowl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>V KOHLI</td>\n",
       "      <td>207</td>\n",
       "      <td>199</td>\n",
       "      <td>6283</td>\n",
       "      <td>113</td>\n",
       "      <td>5</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>S DHAWAN</td>\n",
       "      <td>194</td>\n",
       "      <td>191</td>\n",
       "      <td>5784</td>\n",
       "      <td>106</td>\n",
       "      <td>2</td>\n",
       "      <td>44</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>ROHIT SHARMA</td>\n",
       "      <td>213</td>\n",
       "      <td>208</td>\n",
       "      <td>5611</td>\n",
       "      <td>109</td>\n",
       "      <td>1</td>\n",
       "      <td>40</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>SURESH RAINA</td>\n",
       "      <td>205</td>\n",
       "      <td>200</td>\n",
       "      <td>5528</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>DAVID WARNER</td>\n",
       "      <td>150</td>\n",
       "      <td>150</td>\n",
       "      <td>5449</td>\n",
       "      <td>126</td>\n",
       "      <td>4</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>AB DE WILLIAMS</td>\n",
       "      <td>184</td>\n",
       "      <td>170</td>\n",
       "      <td>5162</td>\n",
       "      <td>133</td>\n",
       "      <td>3</td>\n",
       "      <td>40</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>CHRIS GAYLE</td>\n",
       "      <td>142</td>\n",
       "      <td>141</td>\n",
       "      <td>4965</td>\n",
       "      <td>175</td>\n",
       "      <td>6</td>\n",
       "      <td>31</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>MS DHONI</td>\n",
       "      <td>220</td>\n",
       "      <td>193</td>\n",
       "      <td>4746</td>\n",
       "      <td>84</td>\n",
       "      <td>0</td>\n",
       "      <td>23</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>ROBIN UTHAPPA</td>\n",
       "      <td>193</td>\n",
       "      <td>186</td>\n",
       "      <td>4722</td>\n",
       "      <td>87</td>\n",
       "      <td>0</td>\n",
       "      <td>25</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>GAUTAM GAMBHIR</td>\n",
       "      <td>154</td>\n",
       "      <td>152</td>\n",
       "      <td>4217</td>\n",
       "      <td>93</td>\n",
       "      <td>0</td>\n",
       "      <td>36</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   rank            name  matches  innings  runs  highest  hundreds  fifties  \\\n",
       "0     1         V KOHLI      207      199  6283      113         5       42   \n",
       "1     2        S DHAWAN      194      191  5784      106         2       44   \n",
       "2     3    ROHIT SHARMA      213      208  5611      109         1       40   \n",
       "3     4    SURESH RAINA      205      200  5528      100         1       39   \n",
       "4     5    DAVID WARNER      150      150  5449      126         4       50   \n",
       "5     6  AB DE WILLIAMS      184      170  5162      133         3       40   \n",
       "6     7     CHRIS GAYLE      142      141  4965      175         6       31   \n",
       "7     8        MS DHONI      220      193  4746       84         0       23   \n",
       "8     9   ROBIN UTHAPPA      193      186  4722       87         0       25   \n",
       "9    10  GAUTAM GAMBHIR      154      152  4217       93         0       36   \n",
       "\n",
       "   bowl  \n",
       "0     8  \n",
       "1     3  \n",
       "2     5  \n",
       "3     5  \n",
       "4     0  \n",
       "5    14  \n",
       "6     1  \n",
       "7    27  \n",
       "8     7  \n",
       "9     2  "
      ]
     },
     "execution_count": 372,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 374,
   "id": "550f7c8a-1db1-4b28-b243-584415f30e7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rank</th>\n",
       "      <th>name</th>\n",
       "      <th>matches</th>\n",
       "      <th>innings</th>\n",
       "      <th>runs</th>\n",
       "      <th>highest</th>\n",
       "      <th>hundreds</th>\n",
       "      <th>fifties</th>\n",
       "      <th>bowl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>V KOHLI</td>\n",
       "      <td>207</td>\n",
       "      <td>199</td>\n",
       "      <td>6283</td>\n",
       "      <td>113</td>\n",
       "      <td>5</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>S DHAWAN</td>\n",
       "      <td>194</td>\n",
       "      <td>191</td>\n",
       "      <td>5784</td>\n",
       "      <td>106</td>\n",
       "      <td>2</td>\n",
       "      <td>44</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>ROHIT SHARMA</td>\n",
       "      <td>213</td>\n",
       "      <td>208</td>\n",
       "      <td>5611</td>\n",
       "      <td>109</td>\n",
       "      <td>1</td>\n",
       "      <td>40</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>SURESH RAINA</td>\n",
       "      <td>205</td>\n",
       "      <td>200</td>\n",
       "      <td>5528</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>DAVID WARNER</td>\n",
       "      <td>150</td>\n",
       "      <td>150</td>\n",
       "      <td>5449</td>\n",
       "      <td>126</td>\n",
       "      <td>4</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>AB DE WILLIAMS</td>\n",
       "      <td>184</td>\n",
       "      <td>170</td>\n",
       "      <td>5162</td>\n",
       "      <td>133</td>\n",
       "      <td>3</td>\n",
       "      <td>40</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>CHRIS GAYLE</td>\n",
       "      <td>142</td>\n",
       "      <td>141</td>\n",
       "      <td>4965</td>\n",
       "      <td>175</td>\n",
       "      <td>6</td>\n",
       "      <td>31</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   rank            name  matches  innings  runs  highest  hundreds  fifties  \\\n",
       "0     1         V KOHLI      207      199  6283      113         5       42   \n",
       "1     2        S DHAWAN      194      191  5784      106         2       44   \n",
       "2     3    ROHIT SHARMA      213      208  5611      109         1       40   \n",
       "3     4    SURESH RAINA      205      200  5528      100         1       39   \n",
       "4     5    DAVID WARNER      150      150  5449      126         4       50   \n",
       "5     6  AB DE WILLIAMS      184      170  5162      133         3       40   \n",
       "6     7     CHRIS GAYLE      142      141  4965      175         6       31   \n",
       "\n",
       "   bowl  \n",
       "0     8  \n",
       "1     3  \n",
       "2     5  \n",
       "3     5  \n",
       "4     0  \n",
       "5    14  \n",
       "6     1  "
      ]
     },
     "execution_count": 374,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_new=data[data['hundreds']>0]\n",
    "df_new"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 376,
   "id": "76bb8dd4-d828-46ff-b39f-9332d4909675",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rank</th>\n",
       "      <th>name</th>\n",
       "      <th>matches</th>\n",
       "      <th>innings</th>\n",
       "      <th>runs</th>\n",
       "      <th>highest</th>\n",
       "      <th>hundreds</th>\n",
       "      <th>fifties</th>\n",
       "      <th>bowl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>VIRAt KOHLI</td>\n",
       "      <td>207</td>\n",
       "      <td>199</td>\n",
       "      <td>6283</td>\n",
       "      <td>113</td>\n",
       "      <td>5</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>S DHAWAN</td>\n",
       "      <td>194</td>\n",
       "      <td>191</td>\n",
       "      <td>5784</td>\n",
       "      <td>106</td>\n",
       "      <td>2</td>\n",
       "      <td>44</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>ROHIT SHARMA</td>\n",
       "      <td>213</td>\n",
       "      <td>208</td>\n",
       "      <td>5611</td>\n",
       "      <td>109</td>\n",
       "      <td>1</td>\n",
       "      <td>40</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>SURESH RAINA</td>\n",
       "      <td>205</td>\n",
       "      <td>200</td>\n",
       "      <td>5528</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>39</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>DAVID WARNER</td>\n",
       "      <td>150</td>\n",
       "      <td>150</td>\n",
       "      <td>5449</td>\n",
       "      <td>126</td>\n",
       "      <td>4</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>AB DE WILLIAMS</td>\n",
       "      <td>184</td>\n",
       "      <td>170</td>\n",
       "      <td>5162</td>\n",
       "      <td>133</td>\n",
       "      <td>3</td>\n",
       "      <td>40</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>CHRIS GAYLE</td>\n",
       "      <td>142</td>\n",
       "      <td>141</td>\n",
       "      <td>4965</td>\n",
       "      <td>175</td>\n",
       "      <td>6</td>\n",
       "      <td>31</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   rank            name  matches  innings  runs  highest  hundreds  fifties  \\\n",
       "0     1     VIRAt KOHLI      207      199  6283      113         5       42   \n",
       "1     2        S DHAWAN      194      191  5784      106         2       44   \n",
       "2     3    ROHIT SHARMA      213      208  5611      109         1       40   \n",
       "3     4    SURESH RAINA      205      200  5528      100         1       39   \n",
       "4     5    DAVID WARNER      150      150  5449      126         4       50   \n",
       "5     6  AB DE WILLIAMS      184      170  5162      133         3       40   \n",
       "6     7     CHRIS GAYLE      142      141  4965      175         6       31   \n",
       "\n",
       "   bowl  \n",
       "0     8  \n",
       "1     3  \n",
       "2     5  \n",
       "3     5  \n",
       "4     0  \n",
       "5    14  \n",
       "6     1  "
      ]
     },
     "execution_count": 376,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#to rename\n",
    "df_new.iloc[0,1]=\"VIRAt KOHLI\"\n",
    "df_new"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bdad4c2-e4e1-4162-9223-9935cbf12ae7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#np.random randint function"
   ]
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
