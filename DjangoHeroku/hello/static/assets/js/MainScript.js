class MasterComponent extends React.Component {
  //I Store the word I'm going to send in state at word
  //I return the list of anagrams into state in the nested list at anagrams
  state = {
    word: '',
    anagrams: [],
  };
  //When submit button is pushed word is checked to make sure the length is right
  handleSubmit = () => {
    this.handleConfirmationWordFormat(this.state.word);
  };

  //Confirms whether the word is the right length (4-12 chars) if so then it calls the api
  handleConfirmationWordFormat = (word) => {
    if (word.length < 4) {
      this.setState({anagrams: ['None: No word in dictionary is shorter than 4 letters']});
    } else if (word.length > 12) {
      this.setState({anagrams: ['None: No word in dictionary is longer than 12 letters']});
    } else {
      //If the length is correct-calls the api
      this.handleAPIFetch();
    }
  }

  //any time a new letter is entered or deleted-state is updated accordingly
  handleWordChange = (e) => {
    this.setState({ word: e.target.value });
  };

  //The api which calls the databse-fired only if word is between 4-12 chars
  handleAPIFetch() {
    //My two variables of the api endpoint and data im sending to the db
    const url = '/word_to_check';
    let data_to_send = {"word": this.state.word};

    //The api call
    fetch(url, {
      method: 'POST', //Since i'm accessing db
      body: JSON.stringify(data_to_send), //Sending it in json
      headers:{
        'Content-Type': 'application/json'
      }
    }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(response => this.setState({anagrams: response})); //Where my data is passed to
  }

  render() {
    //Color change for wrong length words
    const noneStyle = {
      color: "red"
    }
    return (
      <div>
        <div>
          <h1><label>Enter a Word To Find Its Anagarams</label></h1>
          <input
            type='text'
            value={this.state.word}
            onChange={this.handleWordChange}
          />
        </div>
        <br></br>
        <div>
          <button
            onClick={this.handleSubmit}>
            Submit Word!
          </button>
        </div>
        <br></br>
        {
        this.state.anagrams.map((anagram, index) => {
          //Tests whether the object is an error ("None:") or a list of anagrams
          if (anagram.slice(0,5) === "None:") {
            //If the word is not the right length
            return <li style={noneStyle} key={index}>{anagram}</li>;
          } else {
            //return a list of anagrams
            return <li key={index}>{anagram}</li>;
          }
        })
      }
    </div>
    );
  }
}

ReactDOM.render(
  <MasterComponent/>,
  document.getElementById("app")
)
