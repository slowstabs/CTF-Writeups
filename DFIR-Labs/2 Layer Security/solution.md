# DFIR Labs - 2 Layer Security

>The police organized a surprise attack to catch the hacker along with all the exhibits at the scene. However, the hacker had foreseen that, so he encrypted his secret file before that. He even sarcastically said "you are too stupid to decrypt my 2-layer security"
> 
> Note: This challenge doesn't have any questions but the flag itself!

As the handout, I was given a linux file system. 

First thing I did was I went to the Desktop folder and there I found a file called `recycle.bin`. Couldn't do much of it since it seemed like gibberish data, might be useful later. Next I went to find `.bashrc_history` but I wasn't there but I found `.zsh_history` which showed certain commands being run on the zsh terminal. Something related encrypting a pdf with gpg and then deleting the original file.

<img width="1229" height="511" alt="image" src="https://github.com/user-attachments/assets/f1698088-50f6-4844-b9e9-7c5a78ea7dea" />

I got stuck here for a while. Eventually I realised there was a `pwsh` run before the renaming of the T3C4U.SOS took place, which indicated something which was done in powershell. Searched a little about linux powershell executions and found that the history of pwsh is in `\2-layer security\home\kalilinux\.local\share\powershell\PSReadLine\ConsoleHost_history.txt`

<img width="1798" height="398" alt="image" src="https://github.com/user-attachments/assets/2f3a26f8-e076-4a02-bd0e-70cea84b7731" />

In that I found a large base64 string which on decrypting and also decrypting the raw inflate, it gave me something that looks like a script. 

```
iEX ((("{40}{19}{25}{46}{15}{11}{41}{20}{14}{48}{33}{47}{37}{35}{2}{1}{31}{23}{18}{8}{45}{9}{39}{28}{24}{43}{38}{27}{53}{13}{36}{49}{16}{30}{17}{26}{21}{12}{0}{51}{4}{6}{10}{50}{5}{32}{34}{52}{42}{22}{29}{3}{44}{7}"-f '        }

        YPMencryptor = YPMaesMan','aged = New-Object System.Security.Cryptograp','  YPMaesMan','{
        YPMshaManaged.Dispose()
 ','r()
        YPMencryptedBytes = YPMencryptor.TransformFinal','edBytes
        YPMaesManaged.Dispose()
                
        if (YPMPath) {
         ','Block(YPMplainBytes, 0, YPMplainBytes.Length)
        YPMen','se()
    }
}','raphy.CipherMode]::CBC
','ed.Padding = [System.Security.Cryptography.PaddingMode]::Z','cryptedBytes = YPMaesManaged','m
    (','::ReadAllBytes(YPMFile.FullName)
            YPMoutPath = YPMFile.FullName + jnO.SOSjnO
','sEOk))
                
        if (Y','arameterSetName = jnOCryptFilejnO)]
        [String]YPMPath
    )

    Begin {
        YPMshaMan','ra','M','
             ','ystem.Security.Cryptog','()]
    [Outpu','(Mandatory = YPMtrue, P',' = [System.IO.File]','e
            return jnOFile encrypted to YPMoutP','d
        YPMaesManaged.Mode = [S','sManaged.BlockSize','t','   Write-Error -Message jnOFile not found!jnO
                break
            }
            YPMplainBytes',' ','      YPMae','athjnO
        }
    }


    End ','Path -ErrorAction SilentlyContinue
            if (!YPMFile.FullName) {
','hy.AesManage','   [System.IO.File]::WriteA','stem.','llBytes(YPMoutPath, YPMencryptedBytes)
      ','256Managed
      ','PMPath) {
            YPMFile = G','ography.SHA','28
','eros
  ','function Encryption {
    [CmdletBinding','
        [Parameter','= YPMFile.LastWriteTim',' = 1','       YPMaesManaged.Dispo','
        YPMaesManag','Type([string])]
    Pa','Security.Crypt','aged = New-Object Sy','et-Item -Path YP','.IV + YPMencrypt','aged.CreateEncrypto','      (Get-Item YPMoutPath).LastWriteTime ','       YPMaesManaged.KeySize = 256
    }

    Process {
        YPMaesManaged.Key = YPMshaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes(EOkYPMencryptedByte')).rePlace(([cHaR]69+[cHaR]79+[cHaR]107),[STRInG][cHaR]39).rePlace(([cHaR]106+[cHaR]110+[cHaR]79),[STRInG][cHaR]34).rePlace(([cHaR]89+[cHaR]80+[cHaR]77),[STRInG][cHaR]36) )
```
Now after I got this, I got lost again so I asked AI what to do, and I found out that `iEX` is short for Invoke-Expression. And replacing iEX with echo basically executes the script which gives us the script, similar to if I had a b64 string and ran `iEX aGVsbG8= | base64 -d` -> `echo aGVsbG8= | base64 -d`. This gave me the script which was used to encrypt the pdf. 

> Powershell wasn't allowing me to run stuff so I found this is how you temporary allow yourself to do it: 
```
powershell -ExecutionPolicy Bypass -File .\fix.ps1
```

The script used for encoding: 

```
function Encryption {
    [CmdletBinding()]
    [OutputType([string])]
    Param
    (
        [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
        [String]$Path
    )

    Begin {
        $shaManaged = New-Object System.Security.Cryptography.SHA256Managed
        $aesManaged = New-Object System.Security.Cryptography.AesManaged
        $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC

        $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::Zeros
        $aesManaged.BlockSize = 128
        $aesManaged.KeySize = 256
    }

    Process {
        $aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes('$encryptedBytes'))

        if ($Path) {
            $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
            if (!$File.FullName) {

                Write-Error -Message "File not found!"
                break
            }
            $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
            $outPath = $File.FullName + ".SOS"
        }

        $encryptor = $aesManaged.CreateEncryptor()
        $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
        $encryptedBytes = $aesManaged.IV + $encryptedBytes
        $aesManaged.Dispose()

        if ($Path) {
            [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
            (Get-Item $outPath).LastWriteTime = $File.LastWriteTime
            return "File encrypted to $outPath"
        }
    }


    End {
        $shaManaged.Dispose()
        $aesManaged.Dispose()
    }
}
```

Now in the script we can see that the string `$encryptedBytes` is being used as the key to encrypt
