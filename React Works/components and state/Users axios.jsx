import {useEffect,useState} from 'react'
import axios from 'axios'

function Users() {
    const [users , setUsers] = useState([]);
    useEffect(() => {
        axios('https://jsonplaceholder.typicode.com/users')
        .then((response) => setUsers(response.data))
    } , [])

  return (
    <div>
        <h2>Users name</h2>
        <li>
            {users.map((user) => (
                <li key={user.id}>{user.name}</li>
            ))}
        </li>
        <h2>Users email</h2>
        <li>
            {users.map((user) => (
                <li key={user.id}>{user.email}</li>
            ))}
        </li>   
    </div>
  )
}

export default Users
