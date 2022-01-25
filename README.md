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


GET https://lexis-api.herokuapp.com/categories

### Response

```
{
	"Categories": 
	[
		{
			"Category_Name": "4 letters", 
			"Category_Id": "4"
		}, 
		{
			"Category_Name": "5 letters", 
			"Category_Id": "5"
		}, 
		{
			"Category_Name": "6 letters", 
			"Category_Id": "6"
		}, 
		{
			"Category_Name": "7 letters", 
			"Category_Id": "7"
		}
	]
}

```
