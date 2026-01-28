import React , {useState} from 'react'

function Forms() {
    const [isim, setisim] = useState("")
    const [soyisim, setsoyisim] = useState("")
    const [email, setemail] = useState("")
    const [cinsiyet, setcinsiyet] = useState("erkek")
  return (
    <div>
        <div>
            <div>isim: </div>
            <input type="text" placeholder='isim' value={isim} onChange={(e) => setisim(e.target.value)}/>
        </div>
        <div>
            <div >soyisim: </div>  
            <input type="text" placeholder='soyisim' value={soyisim} onChange={(e) => setsoyisim(e.target.value)}/>
        </div>
        <div>
            <div >email: </div>
            <input type="text" placeholder='example@email.com' value={email} onChange={(e) => setemail(e.target.value)}/>
        </div>
        
        <div>
            <div >cinsiyet: </div>
            <select value={cinsiyet} onChange={(e) => setcinsiyet(e.target.value)}>
                <option value="erkek">erkek</option>
                <option value="kadın">kadın</option>
            </select>
        </div>
        <hr />
        <div>isim soyisim: {isim} {soyisim}</div>
        <div>email: {email} </div>
        <div>cinsiyet:{cinsiyet}</div>
    </div>
  )
}

export default Forms
