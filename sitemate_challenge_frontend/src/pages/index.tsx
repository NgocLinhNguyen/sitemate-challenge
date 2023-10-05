import Issues from '@/components/Issues'
import { Stack, Text } from '@chakra-ui/layout'
import Head from 'next/head'

export default function Home() {
  

  return (
    <>
      <Head>
        <title>Issues Management</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Stack spacing={4} mt={5} p={30}>
        <Text fontSize='4xl' as='b' align={'center'}>Issues Management</Text>
        <Issues />
      </Stack>
    </>
  )
}
