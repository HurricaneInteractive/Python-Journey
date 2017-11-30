import React from 'react'

export default class App extends React.Component {
    constructor() {
        super();
        this.state = {
            items: null
        }
    }

    componentDidMount() {
        const _this = this
        fetch('/items', {method: 'GET'})
            .then((resp) => resp.json())
            .then(function(data) {
                  _this.setState({
                      items: data.items
                  })
            })
    }

    render() {
        if (this.state.items == null) {
            return <h1>Loading...</h1>
        }
        
        return (
            <div className="container">
                <h2>Items from endpoint: <pre>/items</pre></h2>
                <ul>
                    {
                        this.state.items.map((item, index) => {
                            return <li key={index}>{item.id} | {item.name}</li>
                        })
                    }
                </ul>
            </div>
        )
    }
}