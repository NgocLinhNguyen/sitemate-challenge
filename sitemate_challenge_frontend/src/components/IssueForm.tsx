import { Issue } from '@/interfaces'
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
  Button,
  Input,
  Textarea,
  Select,
  VStack,
  useToast,
  FormControl,
  FormLabel,
} from '@chakra-ui/react'
import { useForm, Controller } from 'react-hook-form'

type Props = {
  issue?: Issue
  onSuccess: () => void
}
type FormValues = {
  title: string
  description: string
}

const IssueForm = ({issue, onSuccess}: Props) => {
  const toast = useToast()
  const { isOpen, onOpen, onClose } = useDisclosure()
  const id = issue?.id
  const onCreate = (values: FormValues) => {
    fetch(
      'http://localhost:8000/api/v1/issues/',
      {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values)
      },
    ).then((res) => {
      if (res.ok) {
        toast({
          title: 'Create new issue successfully',
          status: 'success',
          isClosable: true,
        })
        onSuccess()
        onClose()
      } else {
        toast({
          title: 'Create new issue failed',
          status: 'error',
          isClosable: true,
        })
      }
    }).catch((error) => console.log(error))
  }
  const onUpdate = (values: FormValues) => {
    fetch(
      `http://localhost:8000/api/v1/issues/${id}`,
      {
        method: 'PATCH',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values)
      },
    ).then((res) => {
      if (res.ok) {
        toast({
          title: 'Update issue successfully',
          status: 'success',
          isClosable: true,
        })
        onSuccess()
        onClose()
      } else {
        toast({
          title: 'Update issue failed',
          status: 'error',
          isClosable: true,
        })
      }
    }).catch((error) => console.log(error))
  }

  const onSubmit = (values: FormValues) => {
    console.log(values)
    if (id) onUpdate(values)
    else onCreate(values)
  }
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    defaultValues: {
      title: issue?.title || '',
      description: issue?.description || '',
    }
  })

  return (
    <>
      <Button size='sm' onClick={onOpen} colorScheme='blue'>{id ? 'Edit' : 'New issue'}</Button>
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
        <form onSubmit={handleSubmit(onSubmit)}>
          <ModalHeader>{id ? 'Edit Issue' : 'Create new issue'}</ModalHeader>
            <ModalCloseButton />
            <ModalBody>
              <VStack spacing={4}>
                <FormControl isRequired>
                  <FormLabel>Title</FormLabel>
                  <Input {...register('title')} placeholder='Issue title' />
                </FormControl>
                <FormControl isRequired>
                  <FormLabel>Description</FormLabel>
                  <Textarea {...register('description')} placeholder='Description about the issue' />
                </FormControl>
                {/* <FormControl>
                  <Select>
                    {['TODO', 'INPROGRESS', 'INREVIEW', 'PENDING', 'DONE'].map((status, i) => (
                      <option key={i} value={status}>{status}</option>
                    ))}
                  </Select>
                </FormControl> */}
              </VStack>
            </ModalBody>

            <ModalFooter>
              <Button colorScheme='blue' mr={3} type='submit' isLoading={isSubmitting} isDisabled={isSubmitting}>
                {id ? 'Update' : 'Submit'}
              </Button>
              <Button variant='ghost' onClick={onClose}>Cancel</Button>
            </ModalFooter>
          </form>
        </ModalContent>
      </Modal>
    </>
  )
}

export default IssueForm