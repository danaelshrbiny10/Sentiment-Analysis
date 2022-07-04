{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "NLP.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# read data and check for missing"
      ],
      "metadata": {
        "id": "2T5UXHJaow6-"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "r40aAjnRnJaq"
      },
      "outputs": [],
      "source": [
        "from pandas.errors import InvalidIndexError\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "%matplotlib inline\n",
        "# sns.set()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = pd.read_csv('/content/Restaurant_Reviews.tsv', sep='\\t',quoting=3)\n",
        "data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "OgkcJySInZlb",
        "outputId": "d24a9e50-5b42-432c-83eb-ce1f451f1643"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                                Review  Liked\n",
              "0                             Wow... Loved this place.      1\n",
              "1                                   Crust is not good.      0\n",
              "2            Not tasty and the texture was just nasty.      0\n",
              "3    Stopped by during the late May bank holiday of...      1\n",
              "4    The selection on the menu was great and so wer...      1\n",
              "..                                                 ...    ...\n",
              "995  I think food should have flavor and texture an...      0\n",
              "996                           Appetite instantly gone.      0\n",
              "997  Overall I was not impressed and would not go b...      0\n",
              "998  The whole experience was underwhelming, and I ...      0\n",
              "999  Then, as if I hadn't wasted enough of my life ...      0\n",
              "\n",
              "[1000 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e0c2f597-cc97-4c2d-8464-a1e331b2db1d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Review</th>\n",
              "      <th>Liked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Wow... Loved this place.</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Crust is not good.</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Not tasty and the texture was just nasty.</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Stopped by during the late May bank holiday of...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>The selection on the menu was great and so wer...</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>995</th>\n",
              "      <td>I think food should have flavor and texture an...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>Appetite instantly gone.</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>997</th>\n",
              "      <td>Overall I was not impressed and would not go b...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>998</th>\n",
              "      <td>The whole experience was underwhelming, and I ...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>999</th>\n",
              "      <td>Then, as if I hadn't wasted enough of my life ...</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1000 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e0c2f597-cc97-4c2d-8464-a1e331b2db1d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e0c2f597-cc97-4c2d-8464-a1e331b2db1d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e0c2f597-cc97-4c2d-8464-a1e331b2db1d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# inspect data"
      ],
      "metadata": {
        "id": "JxUeKTHp0ydh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M-AtUcNXoEGJ",
        "outputId": "0085732e-2c02-45a8-e1fb-b87ff3aa8728"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1000 entries, 0 to 999\n",
            "Data columns (total 2 columns):\n",
            " #   Column  Non-Null Count  Dtype \n",
            "---  ------  --------------  ----- \n",
            " 0   Review  1000 non-null   object\n",
            " 1   Liked   1000 non-null   int64 \n",
            "dtypes: int64(1), object(1)\n",
            "memory usage: 15.8+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "missing = data.isnull().sum()\n",
        "missing"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tnEFBk9uoIBt",
        "outputId": "a59aeca1-ca35-41b7-8e42-481018afd404"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Review    0\n",
              "Liked     0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Exploring data"
      ],
      "metadata": {
        "id": "WBIh-1nqooKV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data['Liked'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lrF9jaq2otm_",
        "outputId": "f61a2ffe-db25-49c9-b3f5-6ea31b975aa8"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    500\n",
              "0    500\n",
              "Name: Liked, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(x=data['Liked'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "5aRvg6qu1kgq",
        "outputId": "e5af3b5d-d163-4304-8db1-04e0d99f54e7"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f85308e5ad0>"
            ]
          },
          "metadata": {},
          "execution_count": 18
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# data['Review'].value_counts()"
      ],
      "metadata": {
        "id": "inhlnhfh1a-B"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data['Review'].apply(len)\n",
        "# data['Review'].apply(len).max()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TWVABSRZ5HGY",
        "outputId": "8d40bd27-48b0-475c-d158-673d2123acf8"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       24\n",
              "1       18\n",
              "2       41\n",
              "3       87\n",
              "4       59\n",
              "      ... \n",
              "995     66\n",
              "996     24\n",
              "997     50\n",
              "998     91\n",
              "999    134\n",
              "Name: Review, Length: 1000, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data['Review Lettre Count'] = data['Review'].apply(len)\n",
        "data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "rzJcy1tM5l5A",
        "outputId": "fbc609b3-5814-4f4b-99b5-994c16735ae6"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                                Review  Liked  \\\n",
              "0                             Wow... Loved this place.      1   \n",
              "1                                   Crust is not good.      0   \n",
              "2            Not tasty and the texture was just nasty.      0   \n",
              "3    Stopped by during the late May bank holiday of...      1   \n",
              "4    The selection on the menu was great and so wer...      1   \n",
              "..                                                 ...    ...   \n",
              "995  I think food should have flavor and texture an...      0   \n",
              "996                           Appetite instantly gone.      0   \n",
              "997  Overall I was not impressed and would not go b...      0   \n",
              "998  The whole experience was underwhelming, and I ...      0   \n",
              "999  Then, as if I hadn't wasted enough of my life ...      0   \n",
              "\n",
              "     Review Lettre Count  \n",
              "0                     24  \n",
              "1                     18  \n",
              "2                     41  \n",
              "3                     87  \n",
              "4                     59  \n",
              "..                   ...  \n",
              "995                   66  \n",
              "996                   24  \n",
              "997                   50  \n",
              "998                   91  \n",
              "999                  134  \n",
              "\n",
              "[1000 rows x 3 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5483a213-b650-4c30-947f-4cbc202c6f5f\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
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
              "      <th>Review</th>\n",
              "      <th>Liked</th>\n",
              "      <th>Review Lettre Count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Wow... Loved this place.</td>\n",
              "      <td>1</td>\n",
              "      <td>24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Crust is not good.</td>\n",
              "      <td>0</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Not tasty and the texture was just nasty.</td>\n",
              "      <td>0</td>\n",
              "      <td>41</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Stopped by during the late May bank holiday of...</td>\n",
              "      <td>1</td>\n",
              "      <td>87</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>The selection on the menu was great and so wer...</td>\n",
              "      <td>1</td>\n",
              "      <td>59</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>995</th>\n",
              "      <td>I think food should have flavor and texture an...</td>\n",
              "      <td>0</td>\n",
              "      <td>66</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>996</th>\n",
              "      <td>Appetite instantly gone.</td>\n",
              "      <td>0</td>\n",
              "      <td>24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>997</th>\n",
              "      <td>Overall I was not impressed and would not go b...</td>\n",
              "      <td>0</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>998</th>\n",
              "      <td>The whole experience was underwhelming, and I ...</td>\n",
              "      <td>0</td>\n",
              "      <td>91</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>999</th>\n",
              "      <td>Then, as if I hadn't wasted enough of my life ...</td>\n",
              "      <td>0</td>\n",
              "      <td>134</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1000 rows × 3 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5483a213-b650-4c30-947f-4cbc202c6f5f')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-5483a213-b650-4c30-947f-4cbc202c6f5f button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-5483a213-b650-4c30-947f-4cbc202c6f5f');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.iloc[data['Review Lettre Count'].idxmax()][0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "FzuRvs225q9D",
        "outputId": "5ad4402e-3c51-4ed0-c2a6-e5aa5a102dd1"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'The problem I have is that they charge $11.99 for a sandwich that is no bigger than a Subway sub (which offers better and more amount of vegetables).'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    }
  ]
}