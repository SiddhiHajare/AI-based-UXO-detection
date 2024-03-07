const firebaseConfig = {
  apiKey: "AIzaSyBX9mPpvYlUJQbanJG53Q7rhO9mgGc_Nfg",
  authDomain: "uxo-login-sys.firebaseapp.com",
  projectId: "uxo-login-sys",
  storageBucket: "uxo-login-sys.appspot.com",
  messagingSenderId: "493371329140",
  appId: "1:493371329140:web:dc481f5b055c3fdb291f21",
  measurementId: "G-BQHF1C5SRF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

//Initialize variable
const auth = firebase.auth()
const database = firebase.database()

function register (){

  email = document.getElementById('email').value
  password = document.getElementById('password').value
  first_name = document.getElementById('first_name').value
  last_name = document.getElementById('last_name').value

  //validate input fields
  if(validate_email(email) == false || validate_password == false){
    alert('Email or Password is incorrect!')
    return 
  }

  if(validate_field(first_name) == false || validate_field(last_name) == false){
    alert('One or more extra field is incorrect!')
    return
  }


  //Auth
  auth.createUserWithEmailAndPassword(email,password)
  .then(function(){
    var user = auth.currentUser

    //Add user to firebase database
    var databse_ref = database.ref()

    //Create User data
    var user_data = {
      email: email,
      first_name: first_name,
      last_name: last_name,
      last_login: Date.now()
    }

    database_ref.child('users/'+ user.uid).set(user_data)


    alert('User Created')
  })
  .catch(function(error){
    var error_code = error.code
    var error_message = error.message

    alert(error_message)
  })
}

function validate_email(email){
  expression = /^[^@]+@\w+(\.\w+)+\w$/

  if(expression.test(email) == true){
    //email is good
    return true
  }
  else{
    return false
  }
}

function validate_password(password){
  //password length<6
  if(password<6){
    return false
  }
  else{
    return true
  }
}

function validate_field(field){
  if(field==null){
    return false
  }

  if(field.length<=0){
    return false
  }
  else{
    return true
  }
}