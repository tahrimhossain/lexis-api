# lexis-api

A REST api made using flask





### Get Words


GET https://lexis-api.herokuapp.com/words/{numberofletters}/{numberofwords}

### Response

```
{
	"NumberOfLetters": 4, 
	"Data": 
	[
		{
			"Word": "PEER", 
			"Hints": 
			[
				{
					"PoS": "Noun", 
					"Meaning": 
					[
						"a person who is of equal standing with another in a group", "a nobleman (duke or marquis or earl or viscount or baron"
					]
				}, 
				{
					"PoS": "Verb", 
					"Meaning": 
					[
						"look searchingly"
					]
				}
			]
		}

		...
		...
		...
	]
}

```



### Get Categories


GET https://lexis-api.herokuapp.com/categories/{uid}

### Response

```
{
	"Categories": 
	[
		{
			"Category_Name": "4 letters", 
			"Category_Id": "4",
			"Best_Score": 5
		}, 
		{
			"Category_Name": "5 letters", 
			"Category_Id": "5",
			"Best_Score": 0
		}, 
		{
			"Category_Name": "6 letters", 
			"Category_Id": "6",
			"Best_Score": 0
		}, 
		{
			"Category_Name": "7 letters", 
			"Category_Id": "7",
			"Best_Score": 0
		}
	]
}

```



### Get Leaderboard


GET https://lexis-api.herokuapp.com/highscore/{numberofletters}

### Response

```
{
	"NumberOfLetters": 4, 
	"Top_Scorers": 
	[
		{
			"User_Id": "TaGfqJ8phqe1QKnK9TRQmUH3DDl2", 
			"Name": "tahrim", 
			"Score": 10
		}, 
		{
			"User_Id": "QZvRVFKsh3MYgSWeCbkxSDo2zAm2", 
			"Name": "Abul", 
			"Score": 5
		}

		...
		...
		...
	]
}

```



### Post Score


POST https://lexis-api.herokuapp.com/updatescore/{numberofletters}/{uid}/{score}

