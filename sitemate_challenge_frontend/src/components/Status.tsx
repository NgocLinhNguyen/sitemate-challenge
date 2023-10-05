import { Tag } from "@chakra-ui/tag"

const mappingColorStatus: Record<string, string> = {
  TODO: 'purple',
  DONE: 'green',
  PENDING: 'red',
  INPROGRESS: 'yellow',
  INREVIEW: 'cyan',
}
const StatusInfo = ({status}: {status: string}) => {
  if (!status) return <Tag size='sm'>UNKNOWN</Tag>
  return <Tag size='sm' colorScheme={mappingColorStatus[status]}>{status}</Tag>
}

export default StatusInfo