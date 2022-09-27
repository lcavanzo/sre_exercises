$PALINDROME=$args[0]
$URL="http://40.113.245.97"

$RESPONSE = Invoke-WebRequest -Uri "$URL/$PALINDROME" -UseBasicParsing 


$RESULTS = $RESPONSE | ConvertFrom-Json

#$RESULTS | FT
## Open a stream writer
$FILE   = 'C:\Users\Luis_Cavanzo\Documents\projects\python\python\palindrome-api\output.txt'
$STREAM = [System.IO.StreamWriter]::new($FILE)

foreach ($RESULT in $RESULTS)
{

#write-host "sorted object: $($RESULT.sorted)"
$STREAM.WriteLine("sorted object: $($RESULT.sorted)")

}

# Close the stream
$STREAM.Close()