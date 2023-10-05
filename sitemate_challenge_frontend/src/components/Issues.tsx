import { Issue } from '../interfaces'
import { useEffect, useRef, useState } from 'react'
import { AgGridReact } from 'ag-grid-react'
import { ColDef } from "ag-grid-community"

import 'ag-grid-community/styles/ag-grid.css'
import 'ag-grid-community/styles/ag-theme-alpine.css'

import StatusInfo from './Status'
import { ButtonGroup } from '@chakra-ui/button'
import DeleteIssue from './DeleteIssue'
import IssueForm from '@/components/IssueForm'
import { Box } from '@chakra-ui/layout'

const Issues = () => {
  const [data, setData] = useState<Issue[]>([])
  const [isLoading, setLoading] = useState(true)
 
  const fetchData = () => {
    fetch('http://localhost:8000/api/v1/issues', {
      mode: 'cors',
      headers: {
        'Access-Control-Allow-Origin': '*'
      }
    })
    .then((res) => res.json())
    .then(({data: {issues}}) => {
      setData(issues)
      setLoading(false)
    })
  }
  useEffect(() => {
    fetchData()
  }, [])

  const columnDefs: ColDef[] = [
    { field: "id" },
    { field: "title" },
    { field: "description" },
    {
      field: "status",
      cellRenderer: ({ data: issue }: {data: Issue}) => (
        <Box mt={2}>
          <StatusInfo status={issue.status} />
        </Box>
      ),
    },
    {
      headerName: "Action",
      cellRenderer: ({ data: issue }: {data: Issue}) => (
        <ButtonGroup>
          <IssueForm issue={issue} onSuccess={fetchData}/>
          <DeleteIssue id={issue.id} onSuccess={fetchData}/>
        </ButtonGroup>
      ),
    }
  ]
  const gridRef = useRef<AgGridReact | null>(null)

  return (
    <>
      <IssueForm onSuccess={fetchData} />
      {isLoading ? <p>Loading...</p> : 
      <div className="ag-theme-alpine" style={{width: "100%", height: 600}}>
        <AgGridReact
          ref={gridRef}
          rowData={data}
          columnDefs={columnDefs}
        />
      </div>
      }
    </>
  );
}

export default Issues