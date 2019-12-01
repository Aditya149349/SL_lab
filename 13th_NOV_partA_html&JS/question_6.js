function longest() {
                var s=document.getElementById("sent").value;
                var words=[];
                words=s.split(" ");
                var long=0;
                for (i=0;i<words.length;i++){
                    if(words[i].length>long)
                        long=words[i].length;
                }
                document.getElementById("res").innerHTML="Length of the longest word: "+long;
            }
