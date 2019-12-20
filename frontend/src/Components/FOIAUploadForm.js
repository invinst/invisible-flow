import React from 'react';

class FOIAUploadForm extends React.Component {

  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
    this.state = {
        resultMsg: ""
    }
  }

  async handleSubmit(event) {
    try {
        event.preventDefault();
        const data = new FormData(event.target);

        const response = await fetch('/foia_response_upload', {
          method: 'POST',
          body: data,
        });

        if(!response.ok){
            throw new Error(response.statusText);
        }
        this.setState({resultMsg: "Your file has been successfully uploaded."});

    } catch(error) {
        this.setState({resultMsg: error + ". Please resolve the issue and try again."});
    }
  }



  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <span>Upload FOIA response:</span>
        <div>
        <select required name="response_type">
            <option value="">Please select response type</option>
            <option value="accused">Accused</option>
            <option value="case_info">Case Information</option>
            <option value="civilian_witness">Civilian Witness</option>
            <option value="complainant">Complainant</option>
            <option value="cpd_witness">CPD Witness</option>
            <option value="investigators">Investigators</option>
            <option value="victim">Victim</option>
        </select>
        </div>
        <div>
        <input type="file" name="foia_response" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"/>
        </div>
        <div>
        <button className='action-button' data-testid='uploadButton'>Upload</button>
        </div>
        <div>
        <span data-testid='resultsBanner'>{this.state.resultMsg}</span>
        </div>
      </form>
    );
  }
}

export default FOIAUploadForm;


