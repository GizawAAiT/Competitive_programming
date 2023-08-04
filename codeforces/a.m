LongestIncreasingSubsequenceLength[arr_List] := Module[{lis = {}},
  Do[
    Module[{idx = FirstPosition[lis, _?(# >= x &)]},
      If[MissingQ[idx],
        AppendTo[lis, x],
        lis[[First[idx]]] = x
      ]
    ],
    {x, arr}
  ];
  Length[lis]
]
n = Input[];
arr = ToExpression[StringSplit[InputString[], " "]];
Print[LongestIncreasingSubsequenceLength[arr]]