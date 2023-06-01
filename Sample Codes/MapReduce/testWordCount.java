public class testWordCount {

	public static class testWordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
		public void map(LongWritable key, Text values Context context) throws IOException, InterruptedException {
			
			StringTokenizer tokenizer = new StringTokenizer(values.toString());

			while (tokenizer.hasMoreTokens()) {
				values.set(tokenizer.nextToken());
				context.write(values, new IntWritable(1));
			}

		}
	}

	public static class testWordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException{

			int count = 0;
			for (IntWritable x:values) {
				count += x.get();
			}
			context.write(key, new IntWritable(count));
		}
	}

	public static void main(String[] args) throws Exception {

		configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "word-count");
		job.setJarByClass(testWordCount.class);
		job.setMapperClass(testWordCountMapper.class);
		job.setReducerClass(testWordCountReducer.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		System.exit(job.waitForCompletion(true) ? 0:1);
	}
}